from pathlib import Path

from files.paths_utils import count_lines, files_larger_than, list_py_files


def test_list_py_files_and_count_lines(tmp_path: Path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    f1 = pkg / "a.py"; f1.write_text("print('a')\n", encoding="utf-8")
    f2 = pkg / "b.py"; f2.write_text("print('b')\nprint('b2')\n", encoding="utf-8")
    f3 = pkg / "c.txt"; f3.write_text("x\n", encoding="utf-8")

    found = list_py_files(pkg)
    names = [p.name for p in found]
    assert names == ["a.py", "b.py"]

    assert count_lines(f1) == 1
    assert count_lines(f2) == 2

def test_files_larger_than(tmp_path: Path):
    base = tmp_path / "data"
    base.mkdir()
    small = base / "small.bin"; small.write_bytes(b"x" * 5)
    big = base / "big.bin"; big.write_bytes(b"x" * 20)

    res = files_larger_than(base, min_bytes=10)
    names = sorted([p.name for p in res])
    assert names == ["big.bin"]
