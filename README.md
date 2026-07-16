# E-Commerce Test Automation Framework
![Tests](https://github.com/aniaess/ecommerce-test-automation-framework/actions/workflows/tests.yml/badge.svg)

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
├── pages/
├── tests/
├── utils/
├── test_data/
├── .github/
│   └── workflows/
├── requirements.txt
├── pytest.ini
└── README.md
```

Generated during test execution:

```text
screenshots/
logs/
allure-results/
allure-report/
```

---

# Features

* Page Object Model implementation
* Reusable fixtures
* Externalized test data
* Automatic browser management
* Automatic screenshots for failed tests
* Individual log file for every test with exception traceback
* Allure HTML reports
* Playwright Expect assertions
* Easy project scalability
*  CI/CD integration with GitHub Actions
* Different browser execution modes for local and CI environments

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

# CI/CD - GitHub Actions

The project includes GitHub Actions workflow for automated test execution.

The pipeline automatically:

* Creates a clean test environment
* Installs Python dependencies
* Installs Playwright browsers
* Runs the Pytest test suite

Workflow location:

```text
.github/workflows/tests.yml
```

Tests are executed automatically after pushing changes to the `main` branch.

## Workflow Artifacts

After each workflow execution, GitHub Actions uploads the following artifacts:

* **allure-results** – raw Allure execution results used for generating HTML reports.
* **screenshots** – screenshots captured automatically for failed tests (if available).

---
# Playwright Execution Mode

The framework supports different browser execution modes depending on the environment.

## Local execution

When running tests locally, Playwright runs in headed mode:
```python
headless=False
```
## CI execution

When running inside GitHub Actions, Playwright automatically switches to headless mode.

This allows tests to execute on Linux runners without a graphical interface.
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

The framework integrates Allure Reports using the `allure-pytest` plugin.

Allure provides:

* Test execution overview
* Passed/failed test information
* Failure details
* Execution history
* Better debugging visibility

Raw results are generated after test execution in:

```text
allure-results/
```

The HTML report can then be generated locally using the Allure CLI.

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

* Automatic publication of Allure HTML reports via GitHub Pages
* Parallel execution using pytest-xdist
* Docker support
* Cross-browser execution
* Environment profiles
* Retry mechanism for flaky tests

# Author

Created as a personal QA Automation portfolio project using Python, Pytest, Playwright, and Allure Report.
