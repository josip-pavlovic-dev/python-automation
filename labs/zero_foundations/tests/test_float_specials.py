import math


def test_float_specials():
    inf = float('inf')
    ninf = float('-inf')
    nan = float('nan')
    assert inf > 1e308 and ninf < -1e308
    assert math.isnan(nan)
    assert not (nan == nan)  # NaN nije jednako ni samom sebi
