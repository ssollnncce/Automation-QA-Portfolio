# Test Cases: Auth (Registration & Login)

System under test: [ParaBank](https://parabank.parasoft.com)
Note: ParaBank resets its database daily — test data (especially usernames) must be generated uniquely per run, not hardcoded.

## Known Findings (from manual exploration)

- All registration form fields are required, **except** Phone.
- The Phone and SSN fields do not validate input format — arbitrary letters/characters are accepted.
- The Username field has no upper length limit (a 100+ character value was accepted).

These points are candidates for a bug report (see `bug-reports/`), not just "quirks"

---

## Registration

| ID | Priority | Scenario | Preconditions | Steps | Expected Result |
|---|---|---|---|---|---|
| TC_AUTH-REG-01 | High | Successful registration with valid data | — | 1. Open /register.htm 2. Fill in all fields with valid data 3. Click Register | Account is created, user is redirected to a welcome page and is logged in |
| TC_AUTH-REG-02 | High | Registration with all required fields empty | — | 1. Leave all fields empty 2. Click Register | Form is not submitted; each required field shows a "required" error |
| TC_AUTH-REG-03 | Medium | Registration with Phone left empty | — | 1. Fill in all fields except Phone 2. Click Register | Registration succeeds (Phone is the only optional field) |
| TC_AUTH-REG-04 | Medium | Registration with a Username that already exists | A user with username `X` already exists | 1. Fill in the form with Username = `X` 2. Click Register | Error: "This username already exists" |
| TC_AUTH-REG-05 | Low (bug candidate) | Registration with letters in the Phone field | — | 1. Set Phone = "abcde" 2. Fill in the rest of the fields validly 3. Click Register | **Actual:** registration succeeds — no format validation. Expected: a format error |
| TC_AUTH-REG-06 | Low (bug candidate) | Registration with letters in the SSN field | — | Same as AUTH-REG-05, for SSN | **Actual:** accepted without an error |
| TC_AUTH-REG-07 | Low (bug candidate) | Registration with an extremely long Username (100+ chars) | — | 1. Set a Username 100+ characters long 2. Fill in the rest of the fields 3. Click Register | **Actual:** accepted without an error — no upper limit exists |
| TC_AUTH-REG-08 | High (bug candidate) | Registration with a SSN that already exists | A user with SSN `X` already exists | 1. Fill in the form with SSN = `X` 2. Click Register | Registration should be blocked, and a validation error should be shown next to the SSN field. <br> **Actual:** Registration completes successfully with no error. The user is redirected to the login/welcome page, with no indication that the SSN was already in use by another account. |

## Login

Decision table (Username × Password combinations):

| ID | Priority | Username | Password | Expected Result |
|---|---|---|---|---|
| TC_AUTH-LOGIN-01 | High | Valid (exists) | Valid (correct) | Successful login, redirect to Account Overview |
| TC_AUTH-LOGIN-02 | High | Valid (exists) | Invalid (wrong) | Confirmed — correctly rejected |
| TC_AUTH-LOGIN-03 | High | Invalid (doesn't exist) | Any | Confirmed — correctly rejected |
| TC_AUTH-LOGIN-04 | Medium | Empty | Any | "Required field" error |
| TC_AUTH-LOGIN-05 | Medium | Any | Empty | "Required field" error |
| TC_AUTH_LOGIN-06 | High | Empty | Empty | "Required field@ error |

---

## Test Design Techniques Applied

- **Equivalence Partitioning** — splitting valid/invalid field values into classes (AUTH-REG-01/02/03)
- **Boundary Value Analysis** — probing extreme values to check for missing constraints (AUTH-REG-07)
- **Decision Table** — systematizing condition combinations for Login (AUTH-LOGIN-01..05)
