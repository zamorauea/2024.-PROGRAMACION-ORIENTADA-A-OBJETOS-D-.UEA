def ingresar_temperaturas():
    temperaturas = [3]
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    print("Ingrese las temperaturas diarias:")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

if __name__ == "__main__":
    main()

