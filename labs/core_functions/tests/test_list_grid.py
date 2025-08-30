def test_grid_gotcha():
    # pravimo spoljnu listu sa 2 reference na ISTU unutrašnju listu
    grid = [[0]*3]*2
    grid[0][0] = 1
    # oba reda dele istu unutrašnju listu
    assert grid == [[1, 0, 0], [1, 0, 0]]
    # provera: id-ovi su isti
    assert id(grid[0]) == id(grid[1])

def test_grid_fix():
    # pravimo 2 nezavisne unutrašnje liste
    grid = [[0]*3 for _ in range(2)]
    grid[0][0] = 1
    # sada su redovi nezavisni
    assert grid == [[1, 0, 0], [0, 0, 0]]
    # provera: id-ovi su različiti
    assert id(grid[0]) != id(grid[1])
