# Test Cases: Transfers

System under test: [ParaBank](https://parabank.parasoft.com) — Transfer Funds

The form contains three fields: Amount (text input), From Account (dropdown), To Account (dropdown).

## Known Findings (from manual exploration)

- The Amount field does not validate its value: 0, negative numbers, and amounts greater than the account balance are all accepted.
- The account dropdowns do not allow entering an arbitrary/non-existent account ID — only a user's own existing accounts can be selected (this is correct behavior, not a bug).
- The dropdowns allow selecting the **same** account as both the source and the destination of a transfer.
- An empty or non-numeric value in Amount does not produce a validation error, but an unhandled server exception ("An internal error has occurred and has been logged") — the application effectively crashes on user input.

All of the above are bug-report candidates. The last one (internal error) is the most serious — it's not a "soft" validation gap, it's an application crash.

---

## Test Cases

| ID | Priority | Scenario | Steps | Expected Result | Actual Result |
|---|---|---|---|---|---|
| TC_TRANSFER-01 | High | Successful transfer with a valid amount between different accounts | 1. Set Amount = a valid value ≤ balance 2. Select different From/To accounts 3. Submit | Transfer completes, balance updated on both accounts | Not verified — needs confirmation |
| TC_TRANSFER-02 | High (bug candidate) | Transfer with Amount = 0 | 1. Amount = 0 2. Different From/To 3. Submit | Error — a zero-amount transfer should be rejected | **Accepted without an error** |
| TC_TRANSFER-03 | High (bug candidate) | Transfer with a negative amount | 1. Amount = -50 2. Different From/To 3. Submit | Validation error | **Accepted without an error** |
| TC_TRANSFER-04 | High (bug candidate) | Transfer amount greater than the account balance | 1. Amount = balance + 1000 2. Different From/To 3. Submit | Error: "insufficient funds" | **Accepted without an error**, account balance goes negative |
| TC_TRANSFER-05 | Medium (bug candidate) | Transfer to the same account it's sent from | 1. From = To = the same account 2. Amount = a valid value 3. Submit | Error — transferring to the same account should not be allowed | Not verified — likely accepted (the dropdown allows this selection) |
| TC_TRANSFER-06 | High (bug candidate) | Non-numeric value entered in Amount | 1. Amount = "abc" 2. Different From/To 3. Submit | Format validation error: "Please enter a valid amount" | **Application crashes** with "An internal error has occurred and has been logged" — an unhandled exception (analogous to a 500), not a clean validation error |
| TC_TRANSFER-07 | Medium | Attempt to select a non-existent account | 1. Open the From/To dropdown | The list contains only the user's real accounts; arbitrary input is not possible | Confirmed — works correctly (not a bug) |
| TC_TRANSFER-08 | High (bug candidate) | Empty value in Amount | 1. Amount = "" (left blank) 2. Different From/To 3. Submit | "Required field" error | **Application crashes** with the same "An internal error has occurred" |

---

## Test Design Techniques Applied

- **Equivalence Partitioning** — value classes for Amount (valid / zero / negative / over balance)
- **Boundary Value Analysis** — the meaningful boundaries of 0 and the account balance
- **Decision Table** — the "same account" × "amount" combination (TC_TRANSFER-05)
