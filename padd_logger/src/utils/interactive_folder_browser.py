from pathlib import Path


def choose_folder(prompt: str, base: Path) -> Path:
    """
    Minimal interactive folder chooser:
      - asks user for a relative path inside `base`
      - returns that directory if it exists, else raises FileNotFoundError
    """
    base = Path(base)
    if not base.exists() or not base.is_dir():
        raise FileNotFoundError(base)

    user_input = input(prompt).strip()
    selected = (base / user_input)

    if not selected.exists() or not selected.is_dir():
        raise FileNotFoundError(selected)

    return selected
