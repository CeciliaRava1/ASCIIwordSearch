# Matrix of ASCII numbers corresponding to the alphabet
# (1,6 to 1,13) - Horizontal right   - alphabet =  97 108 102 97 98 101 116 111
# (6,0 to 6,7)  - Horizontal right   - automaton = '97','117','116','111','109','97','116','97'


# (4,12 to 4,8) - Horizontal left - empty    = 118 97 99 105 111

# (1,7 to 1,13) - Vertical down       - language = 108 101 110 103 117 97 106 101

# (7,3 to 0,3)  - Vertical up      - set = 99 111 110 106 117 110 116 111


asciiMatrix = [['99','110','120','111','119','97','102','108','98','118','122','109','116','97'],
               ['97','97','120','116','111','118','97','108','102','97','98','101','116','111'],
               ['99','106','110','110','116','103','118','101','97','122','97','110','116','97'],
               ['106','105','106','117','105','108','119','110','99','98','116','103','109','108'],
               ['105','118','102','106','98','101','98','103','111','105','99','97','118','110'],
               ['110','99','110','110','99','102','111','117','116','120','108','118','110','101'],
               ['97','117','116','111','109','97','116','97','119','102','102','116','122','118'],
               ['105','98','116','99','109','103','97','106','108','99','122','118','119','97'],
               ['118','119','99','118','111','110','120','101','98','119','119','120','98','106']]

# Alphabet - ASCII equivalents for letters
alphabet = {"a":"97", "n":"110", "o":"111", "f":"102", "j":"106", "u":"117", "t":"116",  "m":"109", "g":"103", "c": "99", "l":"108", "e":"101",
			"v":"118", "i":"105", "b":"98", "w":"119", "x":"120", "z":"122"}

# Words to search
words_to_search = ["alfabeto", "vacio", "automata", "conjunto", "lenguaje"]
# ASCII conversion of search word

# Horizontal search to the right
def searchWordHorizontal(row, word_to_search, direction):
    # Get ASCII values for the search word
    word_ascii = [alphabet[i] for i in word_to_search]

    # Define search direction
    if direction == -1:
        word_ascii.reverse()

    # Variable declarations
    col = 0
    total_columns = 14
    remaining_columns = 0
    rows_traversed = 0
    cols_traversed = 0
    not_found = 0

    # Traverse the 8 rows of the matrix
    while rows_traversed < 8:
        while col < 14:
            # Reset variables
            not_found = 0
            # Compare first character of search word with matrix element
            if asciiMatrix[row][col] == word_ascii[0]:
                # Check if there is space for the word
                remaining_columns = total_columns - col
                # If there is space, continue
                if remaining_columns >= len(word_ascii):
                    cols_traversed = 0
                    while cols_traversed <= len(word_ascii)-1 and not_found != 1:
                        if asciiMatrix[row][col+cols_traversed] == word_ascii[cols_traversed]:
                            cols_traversed += 1
                        else:
                            not_found = 1

                    if not_found != 1:
                        if direction == -1:
                            print(f'The word {word_to_search} is from position {row, col+cols_traversed-1} to {row, col}')
                        else:
                            print(f'The word {word_to_search} is from position {row, col} to {row, col+cols_traversed-1}')
            col += 1

        if col == 14:
            rows_traversed += 1
            row += 1
            col = 0


def searchWordVertical(col, word_to_search, direction):
    # Get ASCII values for the search word
    word_ascii = [alphabet[i] for i in word_to_search]

    # Define search direction
    if direction == -1:
        word_ascii.reverse()

    # Variable declarations
    row = 0
    total_rows = 9
    remaining_rows = 0
    columns_traversed = 0
    rows_traversed = 0
    not_found = 0

    # Traverse the 14 columns of the matrix
    while columns_traversed < 14:
        while row < 9:
            # Reset variables
            not_found = 0
            # Compare first character of search word with matrix element
            if asciiMatrix[row][col] == word_ascii[0]:
                # Check if there is space for the word
                remaining_rows = total_rows - row
                if remaining_rows >= len(word_ascii):
                    rows_traversed = 0
                    while rows_traversed <= len(word_ascii)-1 and not_found != 1:
                        if asciiMatrix[row+rows_traversed][col] == word_ascii[rows_traversed]:
                            rows_traversed += 1
                        else:
                            not_found = 1

                    if not_found != 1:
                        if direction == -1:
                            print(f'The word {word_to_search} is from position {row+rows_traversed-1, col} to {row, col}')
                        else:
                            print(f'The word {word_to_search} is from position {row, col} to {row+rows_traversed-1, col}')
            row += 1

        if row == 9:
            columns_traversed += 1
            col += 1
            row = 0


# Algorithm usage
print("*** - Horizontal search to the right - ***")
for i in range (0,5):
    word_to_search = words_to_search[i]
    searchWordHorizontal(0, word_to_search, 0)

print('\n')

print("*** - Horizontal search to the left - ***")
for i in range (0,5):
    word_to_search = words_to_search[i]
    searchWordHorizontal(0, word_to_search, -1)

print('\n')

print("*** - Vertical search downwards - ***")
for i in range (0,5):
    word_to_search = words_to_search[i]
    searchWordVertical(0, word_to_search, 0)

print('\n')

print("*** - Vertical search upwards - ***")
for i in range (0,5):
    word_to_search = words_to_search[i]
    searchWordVertical(0, word_to_search, -1)
