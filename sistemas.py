import menu, os

def imprimir_matriz(matriz):
    for fila in matriz:
        print(["{0:.3f}".format(x) for x in fila])
    print()

def resolver_sistema(matriz):
    n = len(matriz)

    print("Matriz inicial:")
    imprimir_matriz(matriz)

    for i in range(n):
        # Pivoteo: asegurar que el pivote no sea cero
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    break

        # Normalizar la fila del pivote
        pivote = matriz[i][i]
        if pivote == 0:
            print("El sistema no tiene solución única (pivote nulo).")
            opcion = input("Reintroducir valores? (Si || No): ").lower()
            if opcion == "si":
                main()
            elif opcion == "no":
                menu
    
        for j in range(len(matriz[i])):
            matriz[i][j] /= pivote

        print(f"Normalizando fila {i+1}:")
        imprimir_matriz(matriz)

        # Hacer ceros en las demás filas
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(len(matriz[i])):
                    matriz[k][j] -= factor * matriz[i][j]

        print(f"Haciendo ceros en columna {i+1}:")
        imprimir_matriz(matriz)

    return matriz

def limpiar():
    os.system("cls || clear")

def main():
    limpiar()
    print("Bienvenido al apartado de Resolver sistemas lineales")
    n = int(input("Ingrese el número de filas: "))
    matriz = []

    print("\nIngrese la matriz aumentada:")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i+1} (separar con espacios): ").split()))
        if len(fila) != n + 1:
            raise ValueError("Cada fila debe tener n+1 valores (coeficientes + término independiente).")
        matriz.append(fila)

    print(" ")

    resultado = resolver_sistema(matriz)

    print("Matriz final (identidad con soluciones):")
    imprimir_matriz(resultado)

    print("Conjunto soluciones:")
    for i in range(n):
        print(f"x{i+1} = {resultado[i][-1]:.2f}")
    
    input("\nPresione enter para regresar al menu principal . . . ")
    menu.main()