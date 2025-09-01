def test_shallow_copy_with_int_value():
    d1 = {"y": 3}
    d2 = d1.copy()  # shallow copy

    # oba dict-a imaju istu vrednost, ali int je immutable
    assert d1 == d2
    assert d1 is not d2

    # kada promenimo d2["y"], menjamo celu referencu
    d2["y"] = 100
    # d1 ostaje netaknut
    assert d1["y"] == 3
    assert d2["y"] == 100


def test_shallow_copy_with_list_value_shares_reference():
    d1 = {"y": [2, 3]}
    d2 = d1.copy()  # shallow copy

    # oba dict-a izgledaju isto
    assert d1 == d2
    assert d1 is not d2

    # ali lista je mutable → oba dele istu listu
    d2["y"][0] = 99
    # promena se vidi i u d1
    assert d1["y"][0] == 99
    assert d2["y"][0] == 99


def test_overwriting_breaks_sharing():
    d1 = {"y": [2, 3]}
    d2 = d1.copy()

    # kada potpuno zamenimo referencu u d2, prekidamo deljenje
    d2["y"] = [999]
    assert d1["y"] == [2, 3]
    assert d2["y"] == [999]
