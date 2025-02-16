# Получение строки ключей
def StringKeys(matrix_rows):
    string = []
    for x in matrix_rows:
        string.append(x[0])
    return string

# Печать блоков на консоль
def OutputMatrixToConsole(matrix):
    for string in matrix:
        print(string)

# Сборка расшифрованного сообщения
def DecryptedMessage(matrix_string, matrix_column, decoded_matrix):
    decrypted = ''
    for i in range(1, matrix_string):
        for j in range(1, matrix_column):
            decrypted += decoded_matrix[i][j]
    return decrypted

# Функция расшифровки блоков в матрицу
def Decrypt(string_key, column_key, cipher, blocks, matrix_string, matrix_column):
    # Суммарное количество букв в блоках
    letters_in_message = sum(sum(1 for i in string if i) for string in cipher)

    # Задание размеров расшфированной матрицы
    matrix_column = len(column_key)+1
    matrix_string = int(letters_in_message/len(column_key))+1

    # Создание нулевой матрицы с заголовками
    decoded_matrix = [[0 for x in range(matrix_column)] for y in range(matrix_string)]
    decoded_matrix[0] = [0] + column_key # названия колонок
    j = 0 # позиция в ключах по строкам
    for i in range(1, matrix_string):
        decoded_matrix[i][0] = string_key[j]
        j += 1
        if j >= len(string_key):
            j = 0

    # Сопоставление блока ячейке в матрице
    string_keys = StringKeys(decoded_matrix)
    for i in range(len(blocks)):
        column_index = decoded_matrix[0].index(blocks[i][2])
        index = [m for m, x in enumerate(string_keys) if x == blocks[i][1]]
        string_index = index[blocks[i][3]-1]

        # Добавление элемента в расшифрованную матрицу
        decoded_matrix[string_index][column_index] = blocks[i][0]
    
    # Печать матрицы на консоль
    OutputMatrixToConsole(decoded_matrix)

    # Генерация исходного сообщения
    decrypted = DecryptedMessage(matrix_string, matrix_column, decoded_matrix)
    return decrypted
