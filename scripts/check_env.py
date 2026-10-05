import sys
import subprocess
import shutil
from pathlib import Path

def main():
    problems = 0
    repo_root = Path(__file__).resolve().parent.parent

    # 1. Python version >= 3.10
    v = sys.version_info
    v_str = f"{v.major}.{v.minor}.{v.micro}"
    if (v.major, v.minor) >= (3, 10):
        print(f"[ OK ] Python >= 3.10 (found {v_str})")
    else:
        print(f"[FAIL] Python >= 3.10 required (found {v_str})")
        problems += 1

    # 2. Virtual environment check
    in_venv = (sys.prefix != sys.base_prefix) or ("VIRTUAL_ENV" in str(sys.prefix))
    if in_venv:
        print("[ OK ] running inside a virtual environment")
    else:
        print("[FAIL] running inside a virtual environment")
        print("       -> activate .venv first")
        problems += 1

    # 3. pytest installed
    try:
        import pytest
        print("[ OK ] pytest installed")
    except ImportError:
        print("[FAIL] pytest installed")
        print("       -> pip install -r requirements.txt")
        problems += 1

    # 4. Git available
    git_bin = shutil.which("git")
    if git_bin:
        print("[ OK ] git available")
    else:
        print("[FAIL] git available")
        problems += 1

    # 5. Inside git repo
    git_dir = repo_root / ".git"
    if git_dir.exists():
        print("[ OK ] inside a git repository")
    else:
        print("[FAIL] inside a git repository")
        problems += 1

    # 6. .gitignore present
    gitignore = repo_root / ".gitignore"
    if gitignore.exists() and ".venv" in gitignore.read_text(encoding="utf-8", errors="ignore"):
        print("[ OK ] .gitignore present")
    else:
        print("[FAIL] .gitignore present")
        print("       -> Lab 1 step 5")
        problems += 1

    # 7. README has no TODO left
    readme = repo_root / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8", errors="ignore")
        if "TODO" not in content:
            print("[ OK ] README has no TODO left")
        else:
            print("[FAIL] README has no TODO left")
            print("       -> Lab 1 step 5: write the setup instructions")
            problems += 1
    else:
        print("[FAIL] README.md missing")
        problems += 1

    # 8. Git user.email
    try:
        email = subprocess.check_output(["git", "config", "user.email"], cwd=repo_root, text=True).strip()
        if email:
            print(f"[ OK ] git user.email set ({email})")
        else:
            print("[FAIL] git user.email set")
            problems += 1
    except Exception:
        print("[FAIL] git user.email set")
        problems += 1

    # 9. Starter app imports and answers
    try:
        from assistant.rules import reply
        ans = reply("where is the training office?")
        if "I.101" in ans:
            print("[ OK ] starter app imports and answers")
        else:
            print("[FAIL] starter app imports and answers")
            problems += 1
    except Exception as e:
        print(f"[FAIL] starter app imports and answers ({e})")
        problems += 1

    if problems > 0:
        print(f"\n{problems} problem(s) found.")
        sys.exit(1)
    else:
        print("\nAll checks passed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
