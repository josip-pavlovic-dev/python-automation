from pathlib import Path
from foundations_oop.src.path_walker import PathWalker

def test_path_walker_lists_files(tmp_path: Path):
    (tmp_path / "a.txt").write_text("A")
    (tmp_path / "b.log").write_text("B")
    pw = PathWalker(tmp_path)
    files = [p.name for p in pw.list_files("*.txt")]
    assert files == ["a.txt"]
