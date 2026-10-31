---
name: call-me
description: Phone or text the user's real iPhone or Android through the /call-me app and get their spoken answer back as text. Use when the user says "call me", "ring me", "text me when it's done" or asks the agent to stay reachable while they are away, and when the agent is blocked on a yes/no or a choice while the user is not at the keyboard. Needs the /call-me app and its 10-digit number.
---

# call-me

Use this skill when a decision is blocking the work and the user may be away from the screen, or when the user asks to be called, texted or read a summary out loud. The agent rings the user's phone, the text is read aloud, and what they say back returns as a transcript.

Adapted from the canonical [`call-me`](https://github.com/radres/call-me/tree/main/skill) skill in radres/call-me; see the upstream `SKILL.md` for the `callme` CLI, the Claude Code plugin (replies delivered into a live session, a Stop hook for unasked questions) and pairing details.

## Dependency

- The user runs the /call-me app on iPhone ([App Store](https://apps.apple.com/app/call-me/id6789575165)) or Android ([Google Play](https://play.google.com/store/apps/details?id=com.serdaroztetik.callmeai)). The app needs a paid subscription.
- **My Number** in the app shows a 10-digit user number. It is the only credential: no OAuth, login or API key.
- On a local host, keep it in `~/.aiphone/config.json` as `user_number` (directory 700, file 600) and read it before asking. Never invent a number or reuse one from another user or an example.

## Workflow

1. Before ending a turn on an open question, reach the user first. Once the turn ends the agent cannot contact anyone.
2. Write one short question and say what you will do by default if there is no answer.
3. Call when the answer blocks the work; text when nothing is needed back.
4. On `missed` or `declined`, text the question instead, then continue with the safe default or stop, and say which in the final message.

## Hosted MCP server

Add `https://callmemcp.com/mcp` as a remote MCP server (streamable HTTP). Pass the user number as `to`.

- `call`: rings the phone, reads the text word for word (up to 2000 characters) and listens. `completed` carries the transcript; on `ringing` or `in_call`, pass the `call_id` to `poll_result`.
- `say` / `hang_up`: the line stays open after the first answer for a back-and-forth; pass `keep_open: false` for a one-shot call.
- `text`: one-way message, also the fallback for a missed call.
- `wait_for_reply`: waits for what the user sends back (texts, voicemail transcripts).
- `setup`: returns the download links when no number is available yet.

Reuse the `session_token` from each result so calls and texts stay in one thread on the phone.

## Without MCP: curl

```bash
CALLME_TO=$(jq -r .user_number ~/.aiphone/config.json)

# Ring and block until the spoken answer comes back
curl -sS https://callmemcp.com/ring -H 'content-type: application/json' \
  -d "$(jq -nc --arg to "$CALLME_TO" --arg text "Tests pass. Deploy to prod now?" \
    --arg from "Codex" '{to:$to,text:$text,from:$from}')"

# One-way text, no ring
curl -sS https://callmemcp.com/text -H 'content-type: application/json' \
  -d "$(jq -nc --arg to "$CALLME_TO" --arg body "Build green, PR merged. Nothing needed." \
    --arg from "Codex" '{to:$to,body:$body,from:$from}')"
```

## Rules

- Never call or text the `from` number in a result: it is the agent's own identity, and agents cannot reach each other through /call-me.
- "this /call-me number is not active" means the subscription is not running; tell the user to start it in the app.
- Keep each spoken line short. A call is for a decision, not a log dump; put details in a text.
