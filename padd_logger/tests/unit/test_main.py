# tests/unit/test_main.py
import pytest


def test_main_returns_zero():
    """
    Minimalni ugovor:
    - postoji funkcija `main()` u src/main.py
    - vraća int kod izlaza (0 za uspeh)
    """
    import main  # src/main.py (može biti prazan na početku)

    if not hasattr(main, "main"):
        pytest.xfail("main() not implemented yet")

    rc = main.main()  # type: ignore[attr-defined]
    assert isinstance(rc, int)
    assert rc == 0
