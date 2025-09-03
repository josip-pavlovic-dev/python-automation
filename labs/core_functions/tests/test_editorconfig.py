import pathlib

import pytest

# Sve fajlove koje želimo da proverimo (npr. .py, .md, .yml, .json)
EXTS = {".py", ".md", ".yml", ".yaml", ".json", ".jsonc"}


def list_repo_files():
    root = pathlib.Path(__file__).resolve().parents[1]  # koren repoa
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in EXTS:
            yield path


@pytest.mark.parametrize("file_path", list(list_repo_files()))
def test_no_trailing_whitespace_and_final_newline(file_path):
    content = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()

    # 1) nijedna linija ne sme da se završava whitespace-om
    for i, line in enumerate(content, start=1):
        assert not line.endswith(
            (" ", "\t")
        ), f"{file_path}:{i} ima trailing whitespace"

    # 2) fajl mora da se završava praznim newline-om
    raw = file_path.read_bytes()
    assert raw.endswith(b"\n"), f"{file_path} nema final newline"
