# BUG_AUTH_001: Duplicate SSN is accepted during registration

**Severity:** High — SSN is a unique government-issued identifier by definition; accepting duplicates compromises user identity integrity in a financial system.
**Priority:** High — affects core registration/auth logic, directly relevant to the Auth module.

## Environment

- **URL:** https://parabank.parasoft.com/parabank/register.htm
- **Browser:** Chrome
- **Date tested:** 10.03.2026 10:11PM

## Preconditions

A user is already registered with a known SSN. Example: register a new user via the standard registration flow (see `TC_AUTH-REG-01`) and note the SSN value used — this value will be reused as the "duplicate" in the steps below.

## Steps to Reproduce

1. Go to the registration page.
2. Fill in all fields with valid data, except SSN — set SSN to the same value as the already-registered user from Preconditions.
3. Click "Register".

## Expected Result

Registration should be blocked, and a validation error should be shown next to the SSN field — likely using the existing `customer.ssn.errors` element (confirmed present in the DOM for the empty-SSN required-field case), though the exact rendering for a duplicate-value error is not guaranteed to be identical, since no uniqueness check currently exists to observe.

## Actual Result

Registration completes successfully with no error. The user is redirected to the login/welcome page, with no indication that the SSN was already in use by another account.

## Related Test Case

`TC_AUTH-REG-08` (docs/test-cases/auth.md)
