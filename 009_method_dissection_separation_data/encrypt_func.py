# Выбор номера блока, согласно выражению
def DefineBlock(r, s, n):
    K = n * (r-1) + s
    return K

# Печать блоков на консоль
def OutputBlocksToConsole(blocks):
    i = 1
    for position in blocks:
        print("блок " + str(i) + " содержимое", position)
        i += 1

# Функция шифрование матрицы в блоки
def EncryptSeparationDissectionMethod(matrix, number_matrix_column, number_matrix_blocks, matrix_string, matrix_column):
    # Шаблон для формирования блоков 
    blocks = [[] for i in range(number_matrix_blocks)]

    # Формирование блоков
    for i in range(1, matrix_string):
        for j in range(1, matrix_column):
            position_column = matrix[0][j]
            position_string = matrix[i][0]
            position = DefineBlock(position_string, position_column, number_matrix_column)
            blocks[position-1].append(matrix[i][j])
    
    OutputBlocksToConsole(blocks)
    return blocks
