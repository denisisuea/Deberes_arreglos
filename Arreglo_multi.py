# SEMANA 11
# Busqueda en Arreglo Multidimensional
# Matriz bidimensional 3x3 con valores númericos
numeros = [
	[1, 2, 3],
	[3, 5, 6],
	[7, 8 , 9]
]

# valor que estamos buscando
valor_buscar = 9
# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(numeros)):
	for columna in range(len(numeros[fila])):
		if numeros[fila][columna] == valor_buscar:
			fila_encontrada = fila
			columna_encontrada = columna
			break # Detener la busqueda una vezque se encuentra el valor
	if fila_encontrada != -1:
		break # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontró el valor y mostrar la posición

if fila_encontrada != -1:
	print("Se encontró ", valor_buscar, "en la fila ", fila_encontrada, "y la columna", columna_encontrada)
else: 
	print(valor_buscar, "no se encontró en la matriz.")	