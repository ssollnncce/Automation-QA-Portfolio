# Test Cases: Payments (Bill Pay)

System under test: [ParaBank](https://parabank.parasoft.com) — Bill Pay

The form fields: Payee Name, Address, City, State, Zip Code, Phone, Account, Verify Account, Amount, From Account.

## Known Findings (from manual exploration)

- All fields are required.
- The Payee Name field accepts purely numeric values — there is no data-type validation (the mirror image of the Phone/SSN issue found in Auth, where numeric fields accepted letters).
- The Account field correctly rejects non-numeric (string) input — this validation works as expected.
- The Verify Account field correctly checks that its value matches the Account field.
- The Amount field does not validate its value: 0, negative numbers, and amounts greater than the account balance are all accepted (same pattern as in Transfers).

The Payee Name and Amount findings are bug-report candidates. The Account / Verify Account behavior is confirmed as working correctly — worth noting as a positive finding, not just the bugs.

---

## Test Cases

| ID | Priority | Scenario | Steps | Expected Result | Actual Result |
|---|---|---|---|---|---|
| TC_PAYMENT-01 | High | Successful payment with valid data | 1. Fill in all fields with valid data, including a matching Account/Verify Account 2. Submit | Payment is processed, balance is updated | Not verified — needs confirmation |
| TC_PAYMENT-02 | High | Submission with all required fields empty | 1. Leave all fields empty 2. Submit | Form is not submitted; each required field shows a "required" error | Confirmed — works correctly |
| TC_PAYMENT-03 | Low (bug candidate) | Numeric value entered in Payee Name | 1. Set Payee Name = "12345" 2. Fill in the rest of the fields validly 3. Submit | Validation error — a payee name should not be purely numeric | **Accepted without an error** |
| TC_PAYMENT-04 | Medium | Non-numeric value entered in Account | 1. Set Account = "abc" 2. Fill in the rest of the fields validly 3. Submit | Validation error — account must be numeric | Confirmed — correctly rejected |
| TC_PAYMENT-05 | Medium | Account and Verify Account values do not match | 1. Account = "12345" 2. Verify Account = "54321" 3. Submit | Validation error — values must match | Confirmed — correctly rejected |
| TC_PAYMENT-06 | High (bug candidate) | Payment with Amount = 0 | 1. Amount = 0 2. Fill in the rest of the fields validly 3. Submit | Error — a zero-amount payment should be rejected | **Accepted without an error** |
| TC_PAYMENT-07 | High (bug candidate) | Payment with a negative amount | 1. Amount = -50 2. Fill in the rest of the fields validly 3. Submit | Validation error | **Accepted without an error** |
| TC_PAYMENT-08 | High (bug candidate) | Payment amount greater than the account balance | 1. Amount = balance + 1000 2. Fill in the rest of the fields validly 3. Submit | Error: "insufficient funds" | **Accepted without an error**, account balance goes negative |
| TC_PAYMENT-09 | High (bug candidate, not yet confirmed) | Empty or non-numeric value entered in Amount | 1. Amount = "" or "abc" 2. Fill in the rest of the fields validly 3. Submit | Format/required-field validation error | Not verified — based on the same pattern found in Transfers (TC_TRANSFER-06/08), this likely crashes with "An internal error has occurred" rather than showing a clean validation error; needs confirmation |

---

## Test Design Techniques Applied

- **Equivalence Partitioning** — value classes for Payee Name (text vs. numeric) and Amount (valid / zero / negative / over balance)
- **Boundary Value Analysis** — the meaningful boundaries of 0 and the account balance for Amount
- **Decision Table** — Account vs. Verify Account match/mismatch combinations (TC_PAYMENT-04/05)
