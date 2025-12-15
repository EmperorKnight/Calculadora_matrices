import os

matriz = [
    [3, -2],
    [-4, 6],
]

vector_b = [4,5]

os.system("cls || clear")
# print("Introduzca los valores de la matriz 2x2")
# for i in range(2):
#     fila = []
#     for j in range(2):
#         valores = int(input(f"Introduzca los valores de la posicion {i+1},{j+1}: "))
#         fila.append(valores)
#     matriz.append(fila)

print("Matriz original: ")
for fila in matriz:
    print(fila)
print(f"{vector_b}\n ")

for i in range(len(matriz)):
    pivote = matriz[i][i]
    if pivote == 0:
        for j in range(i+1,len(matriz)):
            if matriz[j][i] != 0:
                matriz[j], matriz[i] = matriz[i], matriz[j]
                vector_b[j], vector_b[i] = matriz[i], matriz[j]
                pivote = matriz[i][i]
                break

    if pivote != 1:
        # Conseguir el pivote
        for j in range(len(matriz)):
            matriz[i][j] /= pivote
        
        vector_b[i] /= pivote
        pivote = matriz[i][i]

        for k in range(len(matriz)):
            if i == k:
                pass
            else:
                matriz[k][i] -= pivote * matriz[k][i]

    if pivote == 1:
        for j in range(len(matriz)):
            if j != i:
                matriz[j][i] -= pivote * matriz[j][i]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] == -0.0 or matriz[i][j == 0.0]:
            matriz[i][j] = 0
        elif matriz[i][j] == 1.0:
            matriz[i][j] = 1

print("Matriz resuelta")
for fila in matriz:
    print(fila)
print(vector_b) 
