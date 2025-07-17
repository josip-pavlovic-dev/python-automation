# 🧠 Copilot Instructions for python-automation

## 📌 Project Overview
This repository is a collection of small, real-world Python automation projects, each in its own subfolder (e.g., `01-file-organizer`, `day02_file_info`, `day03_file_management`, `day04_datetime`).

- Each project is self-contained, with its own `main.py`, `README.md`, and often a `logger.py` for consistent logging.
- Projects are designed for CLI use and focus on file/folder operations, metadata extraction, and automation using only core Python libraries (no frameworks).

## 🛠 Key Patterns & Conventions
- **Logging:** Most projects use a reusable `logger.py` module for timestamped logs. Always check for and use this module for logging actions.
- **Testing:** Projects include `.sh` scripts (for Git Bash) to set up test environments.
- **Documentation:** Each project has a bilingual `README.md` (English/Serbian) describing usage, structure, and learning goals.
- **No external dependencies:** All scripts use only the Python standard library.

## 🧩 Developer Workflows
- **Run scripts:** Use `python main.py` (or the relevant script).
- **Set up test data:** Use `setup_test_files.sh`.
- **Debugging:** Use `logger.py` statements.
- **Add new projects:** Use existing structure, create a new folder with `main.py`, `logger.py`, `README.md`.

## 🔗 Examples
- Use `day03_file_management/logger.py` and `scanner.py` for reusable logic.
- Use `day02_file_info/main.py` for metadata analysis.

## 🔒 Special Notes
- All docs should be bilingual (EN/SR).
- Do not add requirements.txt or pip dependencies.
- Focus on core Python features and libraries.