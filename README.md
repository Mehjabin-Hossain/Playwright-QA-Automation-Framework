# Playwright QA Automation Framework

Professional QA automation starter project for authentication testing using Python, pytest, and Playwright.

## What Is Covered

- Login smoke test
- Logout smoke test
- Page Object Model for maintainable selectors and actions
- Environment-based credentials
- Failure screenshots, videos, and traces through `pytest-playwright`

## Project Structure

```text
.
+-- pages/
|   +-- auth_page.py
+-- tests/
|   +-- test_auth.py
+-- conftest.py
+-- qa_config.py
+-- pytest.ini
+-- requirements.txt
+-- .env.example
+-- .github/workflows/qa.yml
+-- automation_runner.py
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Create a local `.env` file from the example:

```bash
copy .env.example .env
```

Update `.env` with your real QA credentials:

```env
APP_BASE_URL=https://your-test-site.example/
QA_EMAIL=your-email@example.com
QA_PASSWORD=your-password
```

Never commit `.env` to GitHub.

## Run Tests

Run the full suite:

```bash
pytest
```

Run only smoke tests:

```bash
pytest -m smoke
```

Run in headed mode:

```powershell
$env:HEADLESS="false"
pytest
```

In Git Bash or Linux/macOS:

```bash
HEADLESS=false pytest
```

## Reports And Debug Artifacts

On failure, Playwright keeps screenshots, videos, and traces under `test-results/`.

Open a trace:

```bash
playwright show-trace path/to/trace.zip
```

## Simple Runner

The simple script entry point still works:

```bash
python automation_runner.py
```

For professional QA automation, prefer `pytest` because it gives better reporting, fixtures, markers, and CI support.

## GitHub Actions 

The included workflow installs dependencies, verifies Python syntax, and collects tests. It does not run the live login test because GitHub should not have credentials unless you explicitly add repository secrets.

To run the real end-to-end test in CI, add these repository secrets:

- `QA_EMAIL`
- `QA_PASSWORD`
