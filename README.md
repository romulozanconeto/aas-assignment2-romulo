# AAS Assignment 2

This repository contains the complete test plan, source code, unit tests, coverage reports, and execution logs for the second assignment of the Software Artifact Analysis course (Master in Informatics Security, University of Coimbra).

The work applies black-box and white-box dynamic testing techniques (equivalence partitioning, boundary value analysis, control flow testing, data flow testing) to four intentionally vulnerable Python functions extracted from the dataset of Assignment 1.

## Repository structure

aas-assignment2-romulo/<br />
├── src/                      # Vulnerable source code<br />
│   ├── a01_access_control.py<br />
│   ├── a02_crypto.py<br />
│   ├── a03_injection.py<br />
│   └── a08_deserialization.py<br />
├── tests/                    # Unit tests (pytest)<br />
│   ├── conftest.py<br />
│   ├── test_a01_access_control.py<br />
│   ├── test_a02_crypto.py<br />
│   ├── test_a03_injection.py<br />
│   └── test_a08_deserialization.py<br />
├── logs/                     # Execution log files<br />
│   └── test_execution.log<br />
├── htmlcov/                  # Coverage report (generated automatically)<br />
├── requirements.txt          # Python dependencies<br />
├── README.md                 # This file<br />
└── LICENSE                   # MIT license<br />

## Functions under test

| File | Function | Vulnerability (OWASP) |
|------|----------|----------------------|
| a01_access_control.py | get_document(doc_id, user) | A01 – Broken Access Control (blind trust in user.role) |
| a02_crypto.py | store_password(password) | A02 – Cryptographic Failure (MD5 without salt) |
| a03_injection.py | get_user_by_id(user_id, mock_cursor) | A03 – SQL Injection (string concatenation) |
| a08_deserialization.py | load_user_preferences(data_b64) | A08 – Software and Data Integrity Failure (insecure pickle.loads) |

> The A03 case was originally written in JavaScript and converted to Python for a homogeneous test environment. The vulnerability remains unchanged.

## Requirements

- Python 3.10 or higher
- pytest 8.2.0
- pytest-cov 5.0.0

Install dependencies inside a virtual environment:

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate        # Linux/macOS
```
```bash
pip install -r requirements.txt
```

## Running the tests

Execute the test suite with coverage measurement:
```bash
pytest tests/ --cov=src --cov-report=term --cov-report=html
```
- The terminal will show a summary of passed/failed tests and line coverage.
- An interactive HTML report is created in the htmlcov/ directory.

## Test results

All 17 tests pass. Line coverage reaches 100% for the four source files. The main results are:

- A01: vulnerability detected by test_admin_access_via_role_manipulation
- A02: vulnerability detected by test_no_salt_vulnerability
- A03: vulnerability detected by test_sql_injection_bypass
- A08: vulnerability detected by mocking pickle.loads and verifying the call

Detailed defect descriptions can be found in the test plan (Chapter 13).

## Test plan

The full test plan (PDF) is part of the assignment submission. It includes risk analysis, equivalence classes, control flow graphs, data flow analysis, approval criteria, environment setup, and team responsibilities.

## License

This project is licensed under the MIT License – see the LICENSE file for details.

## Author

Romulo Angelo Zanco Neto
romulozanconeto@gmail.com
DEI - Department of Informatics Engineering – FCTUC, University of Coimbra