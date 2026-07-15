# E-Commerce Test Automation Framework

## Overview

This project is a UI Test Automation Framework built with **Python**, **Pytest**, and **Playwright**, following the **Page Object Model (POM)** design pattern.

The framework automates end-to-end user scenarios for the SauceDemo application while focusing on clean architecture, maintainability, scalability, and reusable components.

The project includes:

* Page Object Model architecture
* Pytest fixtures
* External test data (JSON)
* Logging
* Automatic screenshots on test failures
* Allure Reports
* Reusable utility modules
* Playwright browser automation

---

# Technology Stack

* Python 3.x
* Pytest
* Playwright
* Allure Report
* JSON
* Logging
* Page Object Model (POM)

---

# Project Structure

```text
E_commerce_Test_Automation_Framework
│
├── pages/                  # Page Objects
├── tests/                  # Test cases and conftest.py
├── utils/                  # Utilities (logger, data loader, etc.)
├── test_data/              # JSON test data
│
├── screenshots/            # Screenshots for failed tests
├── logs/                   # Log files
├── allure-results/         # Raw Allure results
├── allure-report/          # Generated HTML report
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Features

* Page Object Model implementation
* Reusable fixtures
* Externalized test data
* Automatic browser management
* Automatic screenshots for failed tests
* Individual log file for every test
* Allure HTML reports
* Playwright Expect assertions
* Easy project scalability

---

# Installation

Clone the repository:

```bash
git clone <repository_url>
cd E_commerce_Test_Automation_Framework
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

# Running Tests

Run all tests:

```bash
pytest
```

Run a single test file:

```bash
pytest tests/test_login.py
```

Run a single test:

```bash
pytest tests/test_login.py::test_login_success
```

---

# Running Tests from PyCharm

If tests are executed using a PyCharm Run Configuration, add the following argument:

```text
--alluredir=allure-results
```

Go to:

```
Run → Edit Configurations → Additional Arguments
```

---

# Logging

The framework creates a separate log file for each executed test.

Example:

```text
logs/
    test_login_success.log
    test_open_cart.log
    test_checkout.log
```

Each log contains:

* Test start
* Test result
* Error information
* Screenshot location (if test failed)

---

# Screenshots

Whenever a test fails, a screenshot is automatically captured.

Example:

```text
screenshots/

test_login_success_2026-07-14_20-30-11.png
```

---

# Allure Reports

The framework supports Allure HTML Reports.

## Prerequisites

### Install Java (JDK)

Download and install Java JDK.

Example:

```
Eclipse Temurin JDK
```

After installation configure:

Environment Variable:

```
JAVA_HOME
```

Example:

```
C:\Users\<username>\AppData\Local\Programs\Eclipse Adoptium\jdk-25.x.x
```

Add to PATH:

```
%JAVA_HOME%\bin
```

Verify installation:

```bash
java -version
```

---

### Install Allure Commandline

Using Scoop:

```bash
scoop install allure
```

or using Chocolatey:

```bash
choco install allure-commandline
```

Verify installation:

```bash
allure --version
```

---

# Generate Allure Report

Execute tests:

```bash
pytest
```

Generate report:

```bash
allure generate allure-results -o allure-report --clean
```

Open report:

```bash
allure open allure-report
```

---

# Test Data

Test data is stored separately in JSON files.

Examples include:

* Login credentials
* Checkout information
* Product lists

This approach keeps tests clean and easy to maintain.

---

# Design Pattern

This project follows the **Page Object Model (POM)**.

Each page contains:

* Locators
* Page actions
* Page validations

This keeps tests readable and minimizes duplicated code.

---

# Future Improvements

Possible enhancements:

* GitHub Actions (CI/CD)
* Parallel execution with pytest-xdist
* API testing integration
* Docker support
* Cross-browser execution
* Test retries
* Environment configuration
* Allure attachments (logs & screenshots)

---

# Author

Created as a personal QA Automation portfolio project using Python, Pytest, Playwright, and Allure Report.

