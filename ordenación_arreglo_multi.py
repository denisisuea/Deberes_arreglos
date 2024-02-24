# Ordenación Arreglo multidimensional
#Matriz bidimensional con valores numéricos matriz de 3x3 
def bubble_sort_row(matrix, row):
    # Obtener la fila específica de la matriz
    selected_row = matrix[row]

    # Aplicar el algoritmo Bubble Sort a la fila
    n = len(selected_row)
    for i in range(n):
        for j in range(0, n-i-1):
            if selected_row[j] > selected_row[j+1]:
                selected_row[j], selected_row[j+1] = selected_row[j+1], selected_row[j]

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Matriz bidimensional de ejemplo (3x3)
matrix = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5]
]

# Mostrar la matriz original
print("Matriz Original:")
print_matrix(matrix)

# Seleccionar una fila específica para ordenar (por ejemplo, la primera fila)
row_to_sort = 0

# Ordenar la fila seleccionada usando Bubble Sort
bubble_sort_row(matrix, row_to_sort)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con Fila Ordenada:")
print_matrix(matrix)