import pytest

def multiple_two_numbers(a, b):
    return a * b

def fibo(x):
    n1 = 0
    n2 = 1
    for i in range(0, x):
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp

    return n1

@pytest.mark.math
def test_small_numbers():
    assert multiple_two_numbers(1, 2) == 3, "The multiple must be 2"
    pass

@pytest.mark.math
def test_large_numbers():
    assert multiple_two_numbers(100, 10) == 1000, "The multiple must be 1000"
    pass

@pytest.mark.math
def test_fibo_numbers():
    assert fibo(5) == 5, "failed"
    pass