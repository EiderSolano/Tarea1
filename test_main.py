import pytest
from main import sum, numero_mayor

def test_sum():
    assert sum(2,5) == 7
    print("La funcion suma 1 trabaja correctamente")

def test_sum2():
    assert sum(4,6) == 10
    print("La funcion suma 2 trabaja correctamente")

def test_sum3():
    assert sum(10,6) == 16
    print("La funcion suma 3 trabaja correctamente")

def test_sum4():
    assert sum(1,55) == 56
    print("La funcion suma 4 trabaja correctamente")

def test_sum5():
    assert sum(102,6) == 108
    print("La funcion suma 5 trabaja correctamente")
    
def test_numero_mayor():
    numero_mayor(0.5,2)
    print("La funcion numero mayor 1 no trabaja correctamente")

def test_numero_mayor1():
    numero_mayor(10,30)
    print("La funcion numero mayor 2 no trabaja correctamente")

def test_numero_mayor2():
    numero_mayor(1,99)
    print("La funcion numero mayor 3 no trabaja correctamente")

def test_numero_mayor3():
    numero_mayor(6,52)
    print("La funcion numero mayor 4 no trabaja correctamente")

def test_numero_mayor4():
    numero_mayor(100,300)
    print("La funcion numero mayor 5 no trabaja correctamente")
    
@pytest.mark.parametrize(
    "input_x, input_y, esperando",
    [
        (3, 4, 7),
        (5, sum(5,6), 16),
        (sum(2,1), 5, 8),
    ]
)
def test_sum_params(input_x, input_y, esperando):
    assert sum(input_x, input_y) == esperando
    print("Las funciones parametrizadas trabajan correctamente")
    
if __name__ == '__main__':
    test_sum()
    test_sum2()
    test_sum3()
    test_sum4()
    test_sum5()
    test_numero_mayor()
    test_numero_mayor1()
    test_numero_mayor2()
    test_numero_mayor3()
    test_numero_mayor4()