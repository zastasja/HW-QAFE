def add(x, y):
    return x + y

def div (x, y):
    return x / y

def mult (x, y):
    return x * y

def diff (x, y):
    return x - y

def test():
    assert add(2, 3) == 5, f'Wrong answer, should be {sum(2,3)}'
    assert div(4.6, 2) == 2.3, f'Wrong answer, should be {(4.6/ 2)}'
    assert mult(3, 8) == 24, f'Wrong answer, should be {(3*8)}'
    assert diff(2, 2) == 0, f'Wrong answer, should be zero = 0'

test()