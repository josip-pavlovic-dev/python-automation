from pathlib import Path

import pytest


def test_choose_folder_returns_existing(tmp_path: Path, monkeypatch):
    """
    Minimalni ugovor:
    - `choose_folder(prompt: str, base: Path) -> Path`
    - koristi `input()` za relativnu putanju (u testu je monkeypatch-ujemo)
    - vraća postojeći direktorijum (base / user_input)
    """
    # src/utils/interactive_folder_browser.py
    try:
        from utils import interactive_folder_browser as ifb
    except Exception:
        pytest.xfail("utils/interactive_folder_browser module not implemented yet")
        return

    if not hasattr(ifb, "choose_folder"):
        pytest.xfail("choose_folder() not implemented yet")

    base = tmp_path / "base"
    base.mkdir()
    target = base / "project"
    target.mkdir()

    monkeypatch.setattr("builtins.input", lambda _: "project")

    selected = ifb.choose_folder(prompt="Select:", base=base)  # type: ignore[attr-defined]
    assert selected == target
    assert selected.exists() and selected.is_dir()
