import pytest
pytest.skip("E2E placeholder dok ne završimo v1 logger i main", allow_module_level=True)
from pathlib import Path
from logger import get_logger  # (не морамо га директно користити, али добро је за проверу API-ja)
from utils import interactive_folder_browser as ifb
import main

def test_end_to_end_flow(tmp_path: Path, monkeypatch):
    """
    Minimalni E2E:
      - run_flow(base, log_file) orkestra: inicijalizuje logger, pita za folder, upisuje u log, vrati 0
      - monkeypatch input() da vrati "project"
      - tvrdi: log fajl postoji i sadrži bar jedan INFO red koji pominje selektovani folder
    """
    base = tmp_path / "base"
    base.mkdir()
    target = base / "project"
    target.mkdir()

    log_file = tmp_path / "e2e.log"

    # simuliramo unos korisnika ("project")
    monkeypatch.setattr("builtins.input", lambda _: "project")

    # orkestra funkcija (dodaćemo je u main.py)
    rc = main.run_flow(base=base, log_file=log_file)

    assert rc == 0
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "Selected folder:" in content
    assert str(target) in content
