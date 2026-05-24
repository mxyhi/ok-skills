#!/bin/sh
# planning-with-files: lock the current task_plan.md content with a SHA-256 attestation.
#
# Use after you finalise (or intentionally edit) a plan. The hooks then refuse
# to inject plan content into the model context if the file diverges from the
# attested hash, surfacing a "[PLAN TAMPERED]" warning instead.
#
# Resolution:
#   1. $PLAN_ID env var → ./.planning/$PLAN_ID/
#   2. ./.planning/.active_plan
#   3. Newest ./.planning/<dir>/ by mtime
#   4. Legacy ./task_plan.md at project root
#
# Usage:
#   sh scripts/attest-plan.sh         # attest the active plan
#   sh scripts/attest-plan.sh --show  # print the stored hash
#   sh scripts/attest-plan.sh --clear # remove the attestation (re-open the plan)

set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESOLVER="${SCRIPT_DIR}/resolve-plan-dir.sh"

resolve_plan_file() {
    plan_dir=""
    if [ -f "${RESOLVER}" ]; then
        plan_dir="$(sh "${RESOLVER}" 2>/dev/null)"
    fi
    if [ -n "${plan_dir}" ] && [ -f "${plan_dir}/task_plan.md" ]; then
        printf "%s\n" "${plan_dir}/task_plan.md"
        return 0
    fi
    if [ -f "./task_plan.md" ]; then
        printf "%s\n" "./task_plan.md"
        return 0
    fi
    return 1
}

attestation_path_for() {
    plan_file="$1"
    plan_dir="$(dirname "${plan_file}")"
    if [ "${plan_dir}" = "." ]; then
        # Legacy mode: store at project root.
        printf "%s\n" "./.plan-attestation"
    else
        printf "%s\n" "${plan_dir}/.attestation"
    fi
}

compute_hash() {
    target="$1"
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "${target}" | awk '{print $1}'
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "${target}" | awk '{print $1}'
    else
        printf "ERROR: no sha256 utility available\n" >&2
        return 1
    fi
}

mode="attest"
case "${1:-}" in
    --show)  mode="show"  ;;
    --clear) mode="clear" ;;
    "")      mode="attest" ;;
    *)
        printf "Usage: %s [--show|--clear]\n" "$0" >&2
        exit 2
        ;;
esac

plan_file="$(resolve_plan_file)" || {
    printf "[plan-attest] No task_plan.md found. Create a plan first.\n" >&2
    exit 1
}

attestation_file="$(attestation_path_for "${plan_file}")"

case "${mode}" in
    show)
        if [ -f "${attestation_file}" ]; then
            printf "Plan: %s\n" "${plan_file}"
            printf "Attestation: %s\n" "${attestation_file}"
            printf "SHA-256: %s\n" "$(cat "${attestation_file}")"
        else
            printf "[plan-attest] No attestation set for %s.\n" "${plan_file}"
            exit 1
        fi
        ;;
    clear)
        if [ -f "${attestation_file}" ]; then
            rm -f "${attestation_file}"
            printf "[plan-attest] Cleared attestation for %s.\n" "${plan_file}"
        else
            printf "[plan-attest] No attestation to clear.\n"
        fi
        ;;
    attest)
        hash_val="$(compute_hash "${plan_file}")" || exit 1

        # v2.40: protect the write with an advisory flock when available so
        # concurrent legacy-mode sessions (no PLAN_ID, both at the same project
        # root) cannot corrupt the .plan-attestation file mid-write. Atomic
        # rename of a temp file is the real guarantee on POSIX; flock is the
        # cooperative gate around the rename for slow-disk writes.
        #
        # Note: legacy single-file mode is inherently racey across concurrent
        # sessions because both can edit task_plan.md without coordination. The
        # canonical parallel-session pattern is slug-mode under
        # .planning/<slug>/, where each session pins PLAN_ID and gets its own
        # .attestation file. We surface a hint when concurrent activity is
        # detected.
        if [ -f "${attestation_file}" ]; then
            mtime_now="$(date +%s 2>/dev/null || echo 0)"
            mtime_prev="$(stat -c '%Y' "${attestation_file}" 2>/dev/null \
                || stat -f '%m' "${attestation_file}" 2>/dev/null \
                || echo 0)"
            age=$((mtime_now - mtime_prev))
            if [ "${age}" -ge 0 ] && [ "${age}" -lt 30 ] 2>/dev/null; then
                # If we're in legacy mode (root .plan-attestation) and another
                # session just wrote, warn. Slug-mode files in .planning/<slug>/
                # are per-session by construction; no need to warn there.
                case "${attestation_file}" in
                    *./.plan-attestation|*/.plan-attestation)
                        case "${attestation_file}" in
                            *./.planning/*) : ;;  # slug-mode, ignore
                            *)
                                printf "[plan-attest] Note: %s was modified %ss ago by another process.\n" \
                                    "${attestation_file}" "${age}" >&2
                                printf "[plan-attest] For parallel sessions, prefer slug-mode (init-session.sh <name>) so each session gets its own .attestation file.\n" >&2
                                ;;
                        esac
                        ;;
                esac
            fi
        fi

        tmp_file="${attestation_file}.tmp.$$"
        printf "%s\n" "${hash_val}" > "${tmp_file}" 2>/dev/null || {
            printf "[plan-attest] Failed to write %s\n" "${tmp_file}" >&2
            exit 1
        }
        if command -v flock >/dev/null 2>&1; then
            # Advisory lock around the rename. lock_dir is the dir containing
            # the target file. The {} subshell pattern keeps the lock scoped to
            # the mv call.
            lock_dir="$(dirname "${attestation_file}")"
            (
                flock -w 5 9 || true
                mv -f "${tmp_file}" "${attestation_file}"
            ) 9>"${lock_dir}/.attestation.lock" 2>/dev/null
            rm -f "${lock_dir}/.attestation.lock" 2>/dev/null
        else
            mv -f "${tmp_file}" "${attestation_file}" 2>/dev/null
        fi

        # If mv failed for any reason, fall back to direct write.
        if [ ! -f "${attestation_file}" ]; then
            printf "%s\n" "${hash_val}" > "${attestation_file}"
        fi

        short_hash="$(printf "%s" "${hash_val}" | cut -c1-12)"
        printf "[plan-attest] Locked %s\n" "${plan_file}"
        printf "[plan-attest] SHA-256: %s... (stored in %s)\n" "${short_hash}" "${attestation_file}"
        printf "[plan-attest] Hooks will block injection if the file is modified without re-running this command.\n"
        ;;
esac

exit 0
