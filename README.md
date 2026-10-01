# ParaBank Selenium Automation Framework

Automated UI test suite for **[ParaBank](https://parabank.parasoft.com)** — a realistic demo online banking application — built using **Python** and **Selenium WebDriver**.

This project was built as a hands-on learning exercise to practice real-world Selenium automation concepts across a full banking workflow: login, registration, fund transfers, bill payments, account data retrieval, and profile management.

---

## 🏦 Why ParaBank?

ParaBank was chosen over other demo sites because it offers a genuinely realistic banking workflow — open accounts, transfer funds, pay bills, search transaction history, update customer profiles — rather than just a login/logout shell. It's stable, widely used in the QA community, and has no OTP/CAPTCHA blockers that would make automation impractical, while still presenting real-world challenges like dynamically loaded dropdowns and inconsistent HTML element IDs.

---

## ✅ Modules Automated

| Module | File | What it covers |
|---|---|---|
| Login | `login_test.py` | Valid login, asserts successful navigation to Accounts Overview |
| Registration | `signup_test.py` | Negative test — validates required-field error handling (blank First Name) |
| Fund Transfer | `fund_transfer_test.py` | Transfers funds between two accounts, handles dynamically loaded dropdowns |
| Bill Payment | `bill_pay_test.py` | Fills and submits a full bill payment form, verifies confirmation |
| Accounts Overview | `account_overview_test.py` | Reads and parses the account summary table, verifies account data is displayed |
| Find Transactions | `find_transactions_test.py` | Performs a fresh transfer, then searches for it by amount to verify it appears in transaction history |
| Update Profile | `update_profile_test.py` | Updates customer contact information and verifies the confirmation message |

---

## 🧰 Tech Stack

- **Python 3**
- **Selenium WebDriver** (browser automation)
- **webdriver-manager** (automatic ChromeDriver version handling — no manual driver downloads)

---

## 🧠 Key Selenium Concepts Demonstrated

- **Explicit Waits** (`WebDriverWait` + `expected_conditions`) — no `time.sleep()` used for synchronization
- **Custom wait conditions** using lambda functions, to handle dropdowns that populate asynchronously via AJAX
- **Dropdown handling** via Selenium's `Select` class
- **Reading and parsing HTML tables** (account lists, transaction history) programmatically
- **Robust exception handling** (`try / except / finally`) ensuring the browser always closes cleanly, even on failure
- **Meaningful assertions** — verifying actual outcomes (URL changes, confirmation text, table row counts) rather than relying on indirect signals like page titles that don't change between success and failure states
- **Negative testing** — validating that invalid input (e.g., a blank required field) is correctly rejected, not just that the happy path works

---

## 📁 Project Structure

```
ParaBank-Selenium-Automation-Framework/
├── login_test.py
├── signup_test.py
├── fund_transfer_test.py
├── bill_pay_test.py
├── account_overview_test.py
├── find_transactions_test.py
├── update_profile_test.py
├── requirements.txt
└── README.md
```

Each script is fully self-contained: it launches its own browser session, logs in, performs its specific action, asserts the outcome, and closes the browser — independent of every other script.

---

## ⚙️ How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/prabuuu-afk/ParaBank-Selenium-Automation-Framework.git
   cd ParaBank-Selenium-Automation-Framework
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up a test account**
   Register a demo account manually on [ParaBank](https://parabank.parasoft.com/parabank/register.htm), then update the `USERNAME` / `PASSWORD` variables at the top of whichever script you want to run.

   > Note: `fund_transfer_test.py` and `find_transactions_test.py` require the test account to have **at least two open accounts**, since they transfer funds between accounts.

5. **Run any module individually**
   ```bash
   python login_test.py
   python fund_transfer_test.py
   # etc.
   ```

   Each script prints `TEST PASSED`, `TEST FAILED`, or `TEST ERROR` to the terminal depending on the outcome.

---

## 📝 Design Notes

- **Why no fresh account registration per test run?** ParaBank applies anti-automation (bot-detection) measures when it detects repeated rapid account creation from the same session. To work around this realistically, a single pre-registered test account is reused across modules, and `signup_test.py` is scoped to negative/validation testing instead of full registration.
- **Why one flat script per module instead of a Page Object Model framework?** This version prioritizes clarity and speed for a first automation project — each script can be read top-to-bottom with no abstraction layers. A POM-based refactor (with reusable page classes, `pytest` fixtures, and data-driven test data) is a planned next iteration.

---

## 🚀 Planned Improvements

- Refactor into a Page Object Model (POM) structure
- Migrate to `pytest` with fixtures and parametrized test data (CSV/JSON)
- Add logging and automatic screenshot capture on failure
- Add HTML test execution reports
- Cross-browser execution (Chrome + Edge)
- CI/CD integration (GitHub Actions)

---

## 👤 Author

**Prabu** — Final-year B.Tech IT student, aspiring QA Automation Engineer
