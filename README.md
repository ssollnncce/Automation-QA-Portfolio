[**English**](README.md) | [Русский](README.ru.md)

# QA Portfolio: Auth / Transfers / Payments (ParaBank)

> 🚧 Project in active development. This README is updated as the project progresses — see the "Status" section below.

## About

A QA engineering portfolio project combining manual testing (test design, test cases, bug reports) and automation (API, UI, mobile) for a banking domain — registration/login (**Auth**), fund transfer (**Transfers**), bill payment (**Payments**).

The goal is to demonstrate a full QA workflow: from feature analysis and test case design to automated regression checks and CI setup.

## Systems Under Test

- **Web (UI + API):** [ParaBank](https://parabank.parasoft.com) — a demo online banking application
- **Mobile:** [Sauce Labs My Demo App](https://github.com/saucelabs/my-demo-app-android) — a demo app built for Appium practice

## Tech Stack

| Layer | Tools |
|---|---|
| Test runner | Pytest |
| API tests | Requests |
| UI tests | Selenium, Page Object Model |
| Mobile tests | Appium, Appium-Python-Client, UiAutomator2 |
| CI | GitHub Actions |
| Reporting | Allure |

## Project Structure

```
qa-portfolio/
├── docs/
│   ├── test-plan.md          # test plan: scope, risks, strategy
│   └── test-cases/           # manual test cases (test design techniques)
│       ├── auth.md
│       ├── transfers.md
│       └── payments.md
├── bug-reports/              # bugs found: repro steps, expected/actual, logs
├── tests/
│   ├── api/                  # planned
│   ├── ui/
│   └── mobile/               # planned
├── pages/                    # Page Object classes (UI and mobile)
├── api_clients/               # HTTP request wrapper classes
├── conftest.py                # pytest fixtures
├── pytest.ini
├── requirements.txt
└── README.md
```

## How to Run

```bash
# 1. Clone the repository and enter the project folder
git clone https://github.com/ssolnncce/automation-qa-portfolio.git
cd automation-qa-portfolio

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests by group (markers are registered in pytest.ini)
pytest -m api -v       # API tests only
pytest -m ui -v        # UI tests only
pytest -m mobile -v    # mobile tests only (requires a running Appium Server + emulator)
```

## Test Design Approach

Before any test is automated, each feature is analyzed manually: user scenarios are identified, test design techniques are applied (equivalence partitioning, boundary value analysis, decision tables), and the result is recorded in \`docs/test-cases/\`. Automation covers the most critical and frequently repeated scenarios from that set, rather than being written straight from scratch in code.

## Status

- [x] Project scaffolding, venv, pytest.ini, conftest.py
- [x] Test design & test cases: Auth
- [ ] Test design & test cases: Transfers
- [ ] Test design & test cases: Payments
- [ ] API automation (ParaBank)
- [ ] UI automation (ParaBank, POM)
- [ ] Mobile automation (Appium)
- [ ] Bugs found are documented
- [ ] CI (GitHub Actions)
- [ ] Allure report
