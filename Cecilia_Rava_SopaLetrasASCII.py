#Matriz de numeros ascii que corresponden al alfabeto
#(1,6 a 1,13) - Horizontal derecha   - alfabeto =  97 108 102 97 98 101 116 111
#(6,0 a 6,7)  - Horizontal derecha   - automata = '97','117','116','111','109','97','116','97'


#(4,12 a 4,8) - Horizontal izquierda - vacio    = 118 97 99 105 111

#(1,7 a 1,13) - Vertical abajo       - lenguaje = 108 101 110 103 117 97 106 101

#(7,3 a 0,3)  - Vertical arriba      - conjunto = 99 111 110 106 117 110 116 111


matrizASCII= [['99','110','120','111','119','97','102','108','98','118','122','109','116','97'],
			   ['97','97','120','116','111','118','97','108','102','97','98','101','116','111'],
			  ['99','106','110','110','116','103','118','101','97','122','97','110','116','97'],
			 ['106','105','106','117','105','108','119','110','99','98','116','103','109','108'],
			 ['105','118','102','106','98','101','98','103','111','105','99','97','118','110'],
			 ['110','99','110','110','99','102','111','117','116','120','108','118','110','101'],
			 ['97','117','116','111','109','97','116','97','119','102','102','116','122','118'],
			['105','98','116','99','109','103','97','106','108','99','122','118','119','97'],
			['118','119','99','118','111','110','120','101','98','119','119','120','98','106']]

#Alfabeto - equivalencias ascii con letras
alfabeto = {"a":"97", "n":"110", "o":"111", "f":"102", "j":"106", "u":"117", "t":"116",  "m":"109", "g":"103", "c": "99", "l":"108", "e":"101",
			"v":"118", "i":"105", "b":"98", "w":"119", "x":"120", "z":"122"}

#Palabras a buscar
palabras_buscar = ["alfabeto", "vacio", "automata", "conjunto", "lenguaje"]
#conversion palabra buscar ASCII

#Busqueda horizontal hacia la derecha
def busquedaPalabraHorizontal(fila,palabra_buscar,sentido):
	#Obtencion de palabra a buscar en ASCII
	palabra_buscar_ascii = []
	for i in palabra_buscar:
		palabra_buscar_ascii.append(alfabeto[i])

	#Definicion del sentido de la busqueda
	if sentido == -1:
		palabra_buscar_ascii.reverse()

	#Declaracion de variables
	columna = 0
	columnas_totales = 14
	columnas_restantes = 0
	cantidad_filas_recorridas = 0
	cant_columnas_recorridas = 0
	no_esta = 0

	#Recorrido de las 8 filas de la matriz
		#Recorrido de las 14 columnas de la matriz
	while cantidad_filas_recorridas < 8:
		while columna < 14:
			#Reinicio de variables
			no_esta = 0
			#Comparacion primer caracter palabra buscada con elemento matriz
			if matrizASCII[fila][columna] == palabra_buscar_ascii[0]:
				#Saber si hay espacio para la palabra
				columnas_restantes = columnas_totales - columna
				#Si hay espacio, continuar
				if columnas_restantes >= len(palabra_buscar_ascii) :
					#print(f'la palabra {palabra_buscar_ascii} podria estar en {fila, columna}, hay {columnas_restantes} columnas')

					#Busqueda palabra primera vez, ya tengo la primer letra
					#Reinicio de variables
					cant_columnas_recorridas = 0
					while cant_columnas_recorridas <= len(palabra_buscar_ascii)-1 and no_esta != 1:
						if matrizASCII[fila][columna+cant_columnas_recorridas] == palabra_buscar_ascii[cant_columnas_recorridas]:
							cant_columnas_recorridas += 1
						else:
							no_esta = 1
							#print(f'la palabra {palabra_buscar} no esta en la posicion {fila, columna}')
							#Tengo que volver a buscar la letra igual
					if no_esta != 1:
						if sentido == -1:
							print(f'la palabra {palabra_buscar} esta desde la posicion {fila, columna+cant_columnas_recorridas-1} hasta {fila, columna}')

						else:
							print(f'la palabra {palabra_buscar} esta desde la posicion {fila, columna} hasta {fila, columna+cant_columnas_recorridas-1}')


				#No hay espacio, seguir con la proxima columna
				#else:
					#print(f'la palabra {palabra_buscar_ascii} no podria estar en {fila, columna}, hay {columnas_restantes} columnas')
			columna += 1

		if columna == 14:
			cantidad_filas_recorridas += 1
			fila += 1
			columna = 0



def busquedaPalabraVertical(columna,palabra_buscar,sentido):
	#Obtencion de palabra a buscar en ASCII
	palabra_buscar_ascii = []
	for i in palabra_buscar:
		palabra_buscar_ascii.append(alfabeto[i])

	#Definicion del sentido de la busqueda
	if sentido == -1:
		palabra_buscar_ascii.reverse()

	#Declaracion de variables
	fila = 0
	filas_totales = 9
	filas_restantes = 0
	cantidad_columnas_recorridas = 0
	cant_filas_recorridas = 0
	no_esta = 0

	#Recorrido de las 14 columnas de la matriz
		#Recorrido de las 9 filas de la matriz
	while cantidad_columnas_recorridas < 14:
		while fila < 9:
			#Reinicio de variables
			no_esta = 0
			#Comparacion primer caracter palabra buscada con elemento matriz
			if matrizASCII[fila][columna] == palabra_buscar_ascii[0]:
				#Saber si hay espacio para la palabra
				filas_restantes = filas_totales - fila
				#Si hay espacio, continuar

				if filas_restantes >= len(palabra_buscar_ascii):
					#print(f'la palabra {palabra_buscar_ascii} podria estar en {fila, columna}, hay {filas_restantes} filas')
					cant_filas_recorridas = 0
					while cant_filas_recorridas <= len(palabra_buscar_ascii)-1 and no_esta != 1:
						if matrizASCII[fila+cant_filas_recorridas][columna] == palabra_buscar_ascii[cant_filas_recorridas]:
							cant_filas_recorridas += 1
						else:
							no_esta = 1
							#print(f'la palabra {palabra_buscar} no esta en la posicion {fila, columna}')

					if no_esta != 1:
						if sentido == -1:
							print(f'la palabra {palabra_buscar} esta desde la posicion {fila+cant_filas_recorridas-1, columna} hasta {fila, columna}')

						else:
							print(f'la palabra {palabra_buscar} esta desde la posicion {fila, columna} hasta {fila+cant_filas_recorridas-1, columna}')


				#else:
					#print(f'la palabra {palabra_buscar_ascii} no podria estar en {fila, columna}, hay {filas_restantes} filas')
			fila += 1

		if fila == 9:
			cantidad_columnas_recorridas += 1
			columna += 1
			fila = 0


#Utilizacion del algoritmo
print("*** - Busqueda horizontal a derecha - ***")
#Busqueda horizontal hacia derecha
for i in range (0,5):
	palabra_buscar = palabras_buscar[i]
	busquedaPalabraHorizontal(0, palabra_buscar, 0)

print('\n')

#Busqueda horizontal hacia izquierda
print("*** - Busqueda horizontal a izquierda - ***")
for i in range (0,5):
	palabra_buscar = palabras_buscar[i]
	busquedaPalabraHorizontal(0, palabra_buscar, -1)

print('\n')

#Busqueda vertical hacia abajo
print("*** - Busqueda vertical hacia abajo - ***")
for i in range (0,5):
	palabra_buscar = palabras_buscar[i]
	busquedaPalabraVertical(0, palabra_buscar, 0)

print('\n')

#Busqueda vertical hacia arriba
print("*** - Busqueda vertical hacia arriba - ***")
for i in range (0,5):
	palabra_buscar = palabras_buscar[i]
	busquedaPalabraVertical(0, palabra_buscar, -1)


