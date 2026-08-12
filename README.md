# Bookstore API Automation Test

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Requests](https://img.shields.io/badge/Requests-2.34-green)
![Allure](https://img.shields.io/badge/Allure-2.16-red)

This project contains automated tests for the [DemoQA Bookstore API](https://demoqa.com/swagger) built with Python, Pytest, and Requests for REST API automation testing with request/response logging, Allure reporting, GitHub Actions CI/CD integration, and Telegram notifications.

---

## Project Features

- REST API automation testing
- Service layer pattern for API interaction
- Reusable API client implementation
- Separated test data and configurations
- Provide request and response logging
- Allure reporting integration
- GitHub Actions CI/CD integration
- Automated test result notifications via Telegram

---

## API Testing Coverage

### 🟢 Positive Scenarios

| Module | Scenario | Status |
|:--|:--|:--:|
| **Account** | Register new account | ✅ |
| | Login using valid credentials | ✅ |
| | Generate authentication token | ✅ |
| | Get account details | ✅ |
| | Delete user account | ✅ |
| **BookStore** | Get all books | ✅ |
| | Get a specific book by ISBN | ✅ |
| | Add book to collection | ✅ |
| | Update book in collection | ✅ |
| | Delete book from collection | ✅ |

### 🔴 Negative Scenarios

| Module | Scenario | Status |
|:--|:--|:--:|
| **Account** | Register with empty fields | ✅ |
| | Login using invalid credentials | ✅ |
| | Generate token with empty fields | ✅ |
| | Get account details using invalid user id | ✅ |
| | Delete account using invalid token | ✅ |
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
git clone https://github.com/maolanahadiar/bookstore-api-automation-test.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run Test

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

## Demo Video
Bookstore API Automation Test: [Watch Demo](https://drive.google.com/file/d/1bo-qgWzqSHbZ7GrJrCa3E4KvnL3VdkZ5/view?usp=sharing)

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
[![Bookstore API Automation](https://github.com/maolanahadiar/bookstore-api-automation-test/actions/workflows/api-test.yml/badge.svg)](https://github.com/maolanahadiar/bookstore-api-automation-test/actions/workflows/api-test.yml)

---

## Test Reports

After each CI/CD test execution, the framework automatically generates and delivers the following reports:

- **Allure Report**
  - Detailed test execution results
  - Passed/failed test results
  - [Click here to see the Live Allure Report](https://maolanahadiar.github.io/bookstore-api-automation-test/)

- **API Logs**
  - Request and response details
  - Execution debugging support

- **Telegram Notifications**
  - Automated test result summary
  - Direct links to the Live Allure Report and GitHub Actions Pipeline
    
> Telegram Notification Preview 
<p align="left">
<img src="https://github.com/user-attachments/assets/ca33a1d5-ea4a-48ce-9775-21715afef075" width="500"/>
