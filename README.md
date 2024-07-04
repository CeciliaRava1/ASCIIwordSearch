# SopaLetrasASCII

## Description
This project is an ASCII Word Search Puzzle Solver implemented in Python. It takes a 9x14 matrix filled with ASCII values representing the alphabet and searches for a given set of words in the matrix. The words can be found in any direction: horizontally or vertically.

## ASCII Matrix
The matrix is filled with ASCII values corresponding to the following alphabet: `E = {o, f, j, u, t, a, m, g, c, l, e, v, i, b, w, x, z}`. You can refer to the ASCII table for printable characters on this [ASCII code page](https://elcodigoascii.com.ar/).

### Example Matrix
```python
matrizASCII= [['99','110','120','111','119','97','102','108','98','118','122','109','116','97'],
              ['97','97','120','116','111','118','97','108','102','97','98','101','116','111'],
              ['99','106','110','110','116','103','118','101','97','122','97','110','116','97'],
              ['106','105','106','117','105','108','119','110','99','98','116','103','109','108'],
              ['105','118','102','106','98','101','98','103','111','105','99','97','118','110'],
              ['110','99','110','110','99','102','111','117','116','120','108','118','110','101'],
              ['97','117','116','111','109','97','116','97','119','102','102','116','122','118'],
              ['105','98','116','99','109','103','97','106','108','99','122','118','119','97'],
              ['118','119','99','118','111','110','120','101','98','119','119','120','98','106']]
```

## Words to Find
The words to be found in the matrix are:
- `alfabeto`
- `vacio`
- `automata`
- `conjunto`
- `lenguaje`

## Expected Output
The coordinates of the words in the matrix are as follows:
- "alfabeto" is found from coordinates `(1,6)` to `(1,13)`
- "vacio" is found from coordinates `(4,8)` to `(4,12)`
- "automata" is found from coordinates `(6,0)` to `(6,7)`
- "conjunto" is found from coordinates `(0, 3)` to `(7, 3)`
- "lenguaje" is found from coordinates `(1,7)` to `(8,7)`

## Implementation
### Horizontal Search
The function `busquedaPalabraHorizontal(fila, palabra_buscar, sentido)` searches for the word horizontally in the given row.

### Vertical Search
The function `busquedaPalabraVertical(columna, palabra_buscar, sentido)` searches for the word vertically in the given column.

## Usage
To use the word search solver, run the Python script. It will output the coordinates of the words found in the matrix.

```python
# Example usage
print("*** - Horizontal Search to the Right - ***")
for i in range (0,5):
    palabra_buscar = palabras_buscar[i]
    busquedaPalabraHorizontal(0, palabra_buscar, 0)

print('\n')

print("*** - Horizontal Search to the Left - ***")
for i in range (0,5):
    palabra_buscar = palabras_buscar[i]
    busquedaPalabraHorizontal(0, palabra_buscar, -1)

print('\n')

print("*** - Vertical Search Downwards - ***")
for i in range (0,5):
    palabra_buscar = palabras_buscar[i]
    busquedaPalabraVertical(0, palabra_buscar, 0)

print('\n')

print("*** - Vertical Search Upwards - ***")
for i in range (0,5):
    palabra_buscar = palabras_buscar[i]
    busquedaPalabraVertical(0, palabra_buscar, -1)
```
