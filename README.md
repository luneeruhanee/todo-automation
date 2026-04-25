# TodoMVC Automation Test

This project contains automated test scripts for the TodoMVC web application using Python, Pytest, and Playwright.

## Website Under Test

https://demo.playwright.dev/todomvc/#/

## Tech Stack

- Python
- Pytest
- Playwright
- Pytest-Playwright

## Project Structure

```text
todo-automation/
│
├── tests/
│   ├── test_todo_basic.py
│   ├── test_todo_edit.py
│   ├── test_todo_filter.py
│   ├── test_todo_persistence.py
│   └── test_todo_edge_cases.py
│
├── pages/
│   └── todo_page.py
│
├── data/
│   └── test_data.py
│
├── utils/
│   └── helpers.py
│
├── pytest.ini
├── requirements.txt
└── README.md

