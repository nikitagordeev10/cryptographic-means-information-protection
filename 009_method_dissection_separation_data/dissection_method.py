# Подключение функций шифрования и расшифрования
from encrypt_func import EncryptSeparationDissectionMethod
from decrypt_func import Decrypt
from check_input_data import CheckListValues, FillMessage, DefinePosition

# Входные данные от пользователя
print('\n' + "1) Выберите вид выполняемой операции: '1' - разбиение, '2' - сборка, например: 1")
status = 1

print('\n' + "2) Введите сообщение без пробелов, например: МЕТОДяРАССЕЧЕНИЯ-РАЗНЕСЕНИЯ.")
message = "МЕТОДяРАССЕЧЕНИЯ-РАЗНЕСЕНИЯ."
message = FillMessage(message)

print('\n'+ "3) Введите ключи 4х столбцов в произвольной комбинации, например: [3, 2, 4, 1]")
column_key = [3, 2, 4, 1]
CheckListValues(column_key, 4)

print('\n' + "4) Введите ключи 3х строк, например: [3, 1, 2]")
string_key = [3, 1, 2]
CheckListValues(string_key, 3)

# Обработка входных данных
message_length = len(message)
number_blocks = 12
number_column = 4
number_string = int(number_blocks/number_column)

matrix_column = number_column+1
matrix_string = int(message_length//number_column)+1

# Создание нулевой матрицы с заголовками
matrix = [[0 for x in range(matrix_column)] for y in range(matrix_string)]
matrix[0] = [0] + column_key
j = 0  # позиция в ключах по строкам
for i in range(1, matrix_string):
    matrix[i][0] = string_key[j]
    j += 1
    if j >= len(string_key):
        j = 0

print('\n' + "Текст в виде таблицы состоящей из четырёх столбцов:")
for row in matrix:
    print(row)
print()

# заполение матрицы буквами и сохранение позиций букв
blocks = []
m = 0
for i in range(1, matrix_string):
    for j in range(1, matrix_column):
        matrix[i][j] = message[m]
        add_column = matrix[0][j]
        add_string = matrix[i][0]
        position = DefinePosition(i-1, number_string)
        blocks.append([message[m], add_string, add_column, position])
        m += 1

print("Текст в виде таблицы состоящей из четырёх столбцов:")
for row in matrix:
    print(row)
print()

# Шифрование сообщения в блоки
print("Сформированные, зашифрованные блоки:")
cipher = EncryptSeparationDissectionMethod(matrix, number_column, number_blocks, matrix_string, matrix_column)

# Расшифрованное сообщение сообщения в блоки
print('\n' + "Сформированная, расшифрованная таблица:")
decrypted = Decrypt(string_key, column_key, cipher, blocks, matrix_string, matrix_column)
print('\n' + "Расшифрованное сообщение:", decrypted)
