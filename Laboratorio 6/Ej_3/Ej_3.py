def Leer_ultimo_resultado():
    try:
        with open("operaciones.txt", "r") as archivo:
            ultima_linea = ""
            for linea in archivo:
                ultima_linea = linea
            if ultima_linea:
                ultima_operacion = ultima_linea.strip().split(",")
                return float(ultima_operacion[3])
    except FileNotFoundError:
        return None

def Guardar_operacion(num1, num2, operacion, resultado):
    operaciones = []
    try:
        with open("operaciones.txt", "r") as archivo:
            for linea in archivo:
                operaciones.append(linea)
    except FileNotFoundError:
        pass
    
    operaciones.append(f"{num1},{num2},{operacion},{resultado}\n")
    
    if len(operaciones) > 10:
        operaciones = operaciones[1:]
    
    with open("operaciones.txt", "w") as archivo:
        for op in operaciones:
            archivo.write(op)

def Realizar_operacion(operacion, num1, num2):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            print("Error: División por cero")
            return None
        return num1 / num2
    else:
        print("Operación no válida")
        return None

def Mostrar_registro():
    try:
        with open("operaciones.txt", "r") as archivo:
            print("Registro de operaciones:")
            for linea in archivo:
                num1, num2, op, res = linea.strip().split(",")
                print(f"{num1} {op} {num2} = {res}")
    except FileNotFoundError:
        print("No hay registro de operaciones.")

def Calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("1. Realizar operación")
        print("2. Ver registro de operaciones")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ultimo_resultado = Leer_ultimo_resultado()
            if ultimo_resultado is not None:
                num1 = ultimo_resultado
                print(f"Primer número: {num1}")
            else:
                num1 = float(input("Ingrese el primer número: "))
            
            num2 = float(input("Ingrese el segundo número: "))
            operacion = input("Ingrese la operación (+, -, *, /): ")
            
            resultado = Realizar_operacion(operacion, num1, num2)
            if resultado is not None:
                print(f"Resultado: {resultado}")
                Guardar_operacion(num1, num2, operacion, resultado)
        
        elif opcion == "2":
            Mostrar_registro()
        
        elif opcion == "3":
            print("Gracias por usar la calculadora.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    Calculadora()
