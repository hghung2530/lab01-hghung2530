# Smart Virtual Assistant (Starter)

A lightweight rule-based campus assistant for CSC10014 (Computational Thinking).

## Setup
Prerequisites: Python 3.10+, Git.

```bash
# Clone repository
git clone https://github.com/giahunh2901-prog/lab01-giahunh2901.git
cd lab01-giahunh2901

# Create and activate virtual environment
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On Linux / macOS:
# source .venv/bin/activate

# Install dependencies and local package in editable mode
pip install -r requirements.txt
pip install -e .
```

## Run
Run interactive mode:
```bash
python -m assistant
```
Or run a single query:
```bash
python -m assistant "where is the IT helpdesk?"
# -> IT Helpdesk: room E.005, open Mon-Fri 08:00-17:00.
```

## Test
Run the automated test suite with pytest:
```bash
pytest -q
```

## Check Environment
Verify your workstation setup:
```bash
python scripts/check_env.py
```

## Project Structure
- `src/assistant/`: Core rule-based assistant implementation.
- `data/`: CSV data containing office locations and hours.
- `tests/`: Automated smoke tests.
- `scripts/`: Development environment check scripts.
- `docs/`: Lab documentation and pair verification sheets.

## Troubleshooting
- **No module named assistant**: Ensure `.venv` is activated and run `pip install -e .`.
- **PowerShell script execution disabled**: Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` in PowerShell.