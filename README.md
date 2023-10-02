# SopaLetrasASCII
Sopa de Letras en ASCII. 
Se brinda una matriz 9x14 rellena generada por el alfabeto E = {o, f, j, u, t, a, m, g, c, l, e, v, i, b, w, x, z} en formato ASCII(las respectivas conversiones están en esta página https://elcodigoascii.com.r/), en el apartado de “Caracteres ASCII imprimibles”. Tu tarea es encontrar una serie de palabras dadas en la matriz. Las palabras pueden estar en cualquier dirección: horizontal y vertical. Pregunta: ¿Puedes encontrar las palabras "conjunto", "automata", "lenguaje", "vacio" y “alfabeto” en la matriz proporcionada? Indica las coordenadas de inicio y fin para cada palabra. 

matrizASCII= [['99','110','120','111','119','97','102','108','98','118','122','109','116','97'],
		['97','97','120','116','111','118','97','108','102','97','98','101','116','111'],
		['99','106','110','110','116','103','118','101','97','122','97','110','116','97'],
['106','105','106','117','105','108','119','110','99','98','116','103','109','108'],
	['105','118','102','106','98','101','98','103','111','105','99','97','118','110'],
	['110','99','110','110','99','102','111','117','116','120','108','118','110','101'],
	['97','117','116','111','109','97','116','97','119','102','102','116','122','118'],
	['105','98','116','99','109','103','97','106','108','99','122','118','119','97'],
	['118','119','99','118','111','110','120','101','98','119','119','120','98','106']] 

Output esperado: “alfabeto” se encuentra en las coordenadas (1,6) a (1,13). “vacio” se encuentra en las coordenadas (4,8) a (4,12). “automata” se encuentra en las coordenadas (6,0) a (6,7) . "conjunto" se encuentra en las coordenadas (0, 3) a (7, 3). “lenguaje” se encuentra en las coordenadas (1,7) a (8,7)
