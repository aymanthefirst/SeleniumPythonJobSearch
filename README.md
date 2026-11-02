# Job search automation (Selenium)

**Portfolio:** [aymanthefirst.github.io/portfolio](https://aymanthefirst.github.io/portfolio/)

Python + **Selenium** script that logs into a job board, walks listings, filters by keywords, and applies where the site allows one-click apply. Sample target: **Totaljobs** (search params configurable). Shows the same automation patterns I use for browser workflows and test tooling.

> Educational sample — site markup and ToS change often; run only on accounts you own and with permission.

## Stack

Python 3 · Selenium · Chrome WebDriver

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in values (never commit `.env`).

## Run

```bash
python jobSearch.py
```

Requires Chrome and a matching [ChromeDriver](https://chromedriver.chromium.org/) (or Selenium 4 managed driver).

## Configuration

| Variable | Purpose |
|----------|---------|
| `TOTALJOBS_EMAIL` / `TOTALJOBS_PASSWORD` | Login |
| `JOB_TITLE` / `JOB_LOCATION` | Search |
| `KEYWORDS_TO_AVOID` | Comma-separated substrings; skip jobs whose page contains any |

## Note

Legacy Selenium API (`find_element_by_*`) — kept as-is for this archive; a refresh would use current locators and explicit waits.
