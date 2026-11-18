# Login Handling

## Manual login + a status check

**Do not automate login forms.** Login flows involve CAPTCHA, 2FA and anti-bot checks, and they are different on every site. The CLI works in the user's real browser: the user logs in once by hand, and every later CLI call reuses that session.

## Implementation

### 1. `login-status` is the first command

It must:

- Check the user's identity — call a lightweight authenticated endpoint, or read it from the DOM
- Print `{"ok": true, "data": {"logged_in": true, "user": "<username>"}}` when authenticated
- Print `{"ok": false, "error": {"code": "not_logged_in", "message": "..."}}` and exit 1 when not — an expired session is the same case. The message tells the user to log in to the site in their browser, then run the command again

### 2. Find the auth check endpoint

Follow [Site exploration](site-exploration.md) on the site's home page to find a lightweight call that returns the user's identity (`user_id`, `username`, `is_guest`, …).

### 3. The command

Open the site's tab using the [CLI contract](workflow.md#phase-3-implement), then evaluate the identity call and map the observed fields to `logged_in` / `user`. Only a confirmed guest or unauthenticated response means `not_logged_in`. Preserve network failures, rate limits and server errors as request errors; they do not establish login state.
