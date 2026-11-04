from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(4, 5) == 9
    assert calc.add(1, 1) == 2

def test_subtract():
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(8, 3) == 5

def test_multiply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(3, 3) == 9

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(8, 4) == 2
    assert calc.divide(9, 3) == 3