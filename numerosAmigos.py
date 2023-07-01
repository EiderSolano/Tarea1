# Función para verificar si dos números son amigos
def numeros_amigos(número1, número2):
    suma = 0  # Variable que sumará los divisores de un número
    
    # Suma todos los divisores del número 1
    for i in range(1, número1):
        if número1 % i == 0:
            suma += i
    
    # Si la suma de los divisores del número 1 es igual al número 2
    if suma == número2:
        suma = 0
        # Suma los divisores del número 2
        for i in range(1, número2):
            if número2 % i == 0:
                suma += i
        
        # Si la suma de los divisores de ambos números son iguales
        if suma == número1:
            return f"{número1} y {número2} son amigos"
        else:
            return f"{número1} y {número2} no son amigos"
    else:
        return f"{número1} y {número2} no son amigos"

def main():
    número1 = 220
    número2 = 284
    resultado = numeros_amigos(número1, número2)
    print(resultado)

if __name__ == "__main__":
    main()