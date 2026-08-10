# Bookstore API Automation Framework

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Requests](https://img.shields.io/badge/Requests-2.34-green)
![Allure](https://img.shields.io/badge/Allure-2.16-red)

This project contains automated tests for the [DemoQA Bookstore API](https://demoqa.com/swagger) built with Python, Pytest, and Requests for REST API automation testing with request/response logging, positive and negative test scenario coverage, Allure reporting, GitHub Actions CI/CD integration, and automated test summary notifications through Telegram.

---

## Project Features

- API automation testing using Pytest
- Service layer pattern for API interaction
- Reusable API client implementation
- Separated test data and configurations
- Provide request and response logging
- Allure reporting integration
- GitHub Actions CI/CD integration
- Automated test summary notifications through Telegram

---

## API Testing Coverage

### 🟢 Positive Scenarios

| Module | Scenario | Status |
|:--|:--|:--:|
| **Account** | Create new user account | ✅ |
| | Generate authentication token | ✅ |
| | Login with valid credentials | ✅ |
| | Get user account details | ✅ |
| | Delete user account | ✅ |
| **BookStore** | Get all books | ✅ |
| | Get a specific book by ISBN | ✅ |
| | Add book to collection | ✅ |
| | Update book in collection | ✅ |
| | Delete book from collection | ✅ |

### 🔴 Negative Scenarios

| Module | Scenario | Status |
|:--|:--|:--:|
| **Account** | Register with invalid credentials | 🚧 |
| | Generate token with invalid credentials | 🚧 |
| | Access account with invalid token | 🚧 |
| | Delete account with invalid token | 🚧 |
| **BookStore** | Get book with invalid ISBN | ✅ |
| | Add book without token | ✅ |
| | Add duplicate book to collection | ✅ |
| | Update book with invalid ISBN | ✅ |
| | Delete book without token | ✅ |

---

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

---

## Installation

Clone repository:

```bash
git clone https://github.com/maolanahadiar/bookstore-api-automation-framework.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Test

Run all tests:

```bash
pytest
```

Run & generate Allure report:

```bash
pytest --alluredir=reports/allure-results
```

Open Allure report:

```bash
allure serve reports/allure-results
```

---

## CI/CD

GitHub Actions pipeline automatically runs API tests on:

- Push
- Pull Request
- Manual Trigger

Pipeline flow:

```
Checkout Repository
   |
Setup Python Environment
   |
Install Dependencies
   |
Install Allure CLI
   |
Run API Tests
   |
Generate Allure Report
   |
Deploy Allure Report to GitHub Pages
   |
Upload Test Artifacts & Logs
   |
Send Test Summary Notification to Telegram
```
#### Latest Execution Status:
[![Bookstore API Automation](https://github.com/maolanahadiar/book-store-api-automation-framework/actions/workflows/api-test.yml/badge.svg)](https://github.com/maolanahadiar/bookstore-api-automation-framework/actions/workflows/api-test.yml)

---

## Test Reports

The framework generates:

- **Allure Report**
  - Test execution summary
  - Passed/failed test results

- **API Logs**
  - Request and response details
  - Execution debugging support

➡️ [Click here to see the Live Allure Report](https://maolanahadiar.github.io/bookstore-api-automation-framework/)
