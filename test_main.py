import pytest
from main import sum, numero_mayor

def test_sum():
    assert sum(2,5) == 7
    print("La funcion suma 1 trabaja correctamente")

def test_sum2():
    assert sum(4,6) == 10
    print("La funcion suma 2 trabaja correctamente")
    
def test_numero_mayor():
    assert numero_mayor(10,2)
    print("La funcion numero mayor trabaja correctamente")
    
@pytest.mark.parametrize(
    "input_x, input_y, esperando",
    [
        (3, 4, 7),
        (5, sum(5,6, 16)),
        (sum(2,1), 5, 8),
    ]
)
def test_sum_params(input_x, input_y, esperando):
    assert sum(input_x, input_y) == esperando
    print("Las funciones parametrizadas trabajan correctamente")
    
if __name__ == '__main__':
    test_sum()
    test_numero_mayor()
    test_sum2()