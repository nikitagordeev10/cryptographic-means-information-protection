# ##################### НАСТРОЙКИ ОКРУЖЕНИЯ #####################
# Импорт библиотек
import math

# ##################### СТАТИСТИКА #####################

# Функция вывода данных ШИФРОВАНИЕ
def print_data_encode(original_sequence, checksum_vector, result_vector, checksum_matrix):
    print("Матрица контрольного суммирования:")
    print("  i  [*, *, 1, *, 2, 3, 4, *, 5, 6, 7, 8, 9]")
    print("  j  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]")

    # Печатаем матрицу контрольного суммирования (0, 1, 0, ...)
    c = 0 # столбцы
    for i in checksum_matrix:
        print(f"a[{c + 1}] {i}")
        c += 1

    # Исходная последовательность
    print(f"  b  [_, _, {original_sequence[0]}, _, {original_sequence[1]}, {original_sequence[2]}, {original_sequence[3]}, _, {original_sequence[4]}, {original_sequence[5]}, {original_sequence[6]}, {original_sequence[7]}, {original_sequence[8]}]")
    
    #  Биты резервных позиций
    print(f"beta [{checksum_vector[0]}, {checksum_vector[1]}, _, {checksum_vector[2]}, _, _, _, {checksum_vector[3]}, _, _, _, _, _]")
    
    # Получившийся вектор 
    print(f"b[t] {result_vector}")


# Функция вывода данных РАСШИФРОВКА
def print_data_decode(checksum_vector, place_error):
    #  Биты резервных позиций
    print(f"s[r] {checksum_vector}")

    #  Вывод ошибки
    if place_error != 0:
        print(f"Ошибка в {place_error} бите")
    else:
        print("Нет ошибок!")
        
# ##################### ЗАПОЛНЕНИЕ МАТРИЦ #####################

# Функция заполнения матрицы контрольного суммирования (сверху вниз, слева направо)
def completed_checksum_matrix(checksum_matrix): 
    for i in range(13):
        sequence_length = i + 1
        for j in range(4):
            checksum_matrix[j][i] = sequence_length % 2
            sequence_length //= 2


# ##################### ОБЩАЯ ЧАСТЬ — ШИФРОВАНИЕ И РАСШИФРОВАНИЕ #####################

# Получение данных. Заполнение матрицы
def get_data_fill_matrix(sequence_length):
    # Получение данных. Запись в массив. Преобразование элементов массива к типу int
    try:
        original_sequence = list(input(f"Введите последовательность длинной {sequence_length}: "))
        original_sequence = list(map(int, original_sequence))
    except:
        print("Ошибка в вводе данных!")
        exit(-1)

    # заготовка (для разработки и тестирования)
    if original_sequence[0] == 1 and len(original_sequence) == 1:
        print("Использован заготовленный вариант: 101101010")
        original_sequence = [1, 0, 1, 1, 0, 1, 0, 1, 0]

    if original_sequence[0] == 2 and len(original_sequence) == 1:
        print("Использован заготовленный вариант: 0011111001010")
        original_sequence = [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0]


    # Проверка на корректность введённой последовательности
    for i in original_sequence:
        if (i != 0 and i != 1) or len(original_sequence) != sequence_length:
            print("Ошибка в вводе данных!\n")
            exit(-1)

    # Создание матрицы контрольного суммирования (4 столбца, 13 строк, заполнение "0")
    checksum_matrix = []
    for i in range(4):
        checksum_matrix.append([])
        for j in range(13):
            checksum_matrix[i].append(0)

    # Функция "заполнить матрицу контрольного суммирования"
    completed_checksum_matrix(checksum_matrix)

    return original_sequence, checksum_matrix

# ##################### ШИФРОВАНИЕ #####################

# Функция кодирования бинарной последовательности данных
def encode():
    sequence_length = 9 # Вариант 1

    # ---------------------------------------------------------------
    # Получение данных. Заполнение матрицы
    original_sequence, checksum_matrix = get_data_fill_matrix(sequence_length)
    # ---------------------------------------------------------------

    # Добавляем места, куда потом вставим контрольные битов
    result_vector = []
    pos = 0
    for i in range(13):
        k = math.log2(i+1) % 1  # вычисление степень двойки
        if k == 0:
            result_vector.append(0)
        else:
            result_vector.append(original_sequence[pos]) # вставляем нули на место куда подставятся числа
            pos += 1

    # Нахождение вектора контрольных сумм (St)
    checksum_vector = []
    for i in range(4):
        summ = 0
        for j in range(13):
            summ += result_vector[j] * checksum_matrix[i][j] # (побитовое и) и подсчёт единиц
        checksum_vector.append(summ % 2) # чётность → 0 / 1 

    # Получаем кодовое слово, вставляя биты вектора контрольных сумм
    pos = 0
    for i in range(13):
    # подставляем в степени двойки
        if math.log2(i+1) % 1 == 0:
            result_vector[i] = checksum_vector[pos]
            pos += 1

    # Печать результата пользователю
    print_data_encode(original_sequence, checksum_vector, result_vector, checksum_matrix)

# ##################### РАСШИФРОВКА #####################

# Функция декодирования бинарной последовательности данных
def decode():
    sequence_length = 13

    # ---------------------------------------------------------------
    # Получение данных. Заполнение матрицы
    original_sequence, checksum_matrix = get_data_fill_matrix(sequence_length)
    # ---------------------------------------------------------------

    # Нахождение вектора контрольных сумм (St)
    checksum_vector = []
    for i in range(4):
        summ = 0
        for j in range(13):
            summ += original_sequence[j] * checksum_matrix[i][j] # (побитовое и) и подсчёт единиц
        checksum_vector.append(summ % 2) # чётность → 0 / 1 

    # Сумма битых ячеек
    place_error = 0
    for i in range(4):
        place_error += checksum_vector[i] * 2**i

    # Печать результата пользователю
    print_data_decode(checksum_vector, place_error)

# ##################### ИНТЕРФЕЙС ПОЛЬЗОВАТЕЛЯ #####################

def main():
    while True:
        user_select = int(input("Выберите режим:\n" + "(1): Кодирование методом Хэмминга\n" +
                          "(2): Проверка методом Хэмминга\n" + "(3): Выход\n" + "Ваш выбор: "))

        # Кодирование методом Хэмминга
        if user_select == 1:
            encode()

        # Проверка методом Хэмминга
        elif user_select == 2:
            decode()
        
        # Выход
        elif user_select == 3:
            exit(0)

# ##################### ЗАПУСК ПРОГРАММЫ #####################

if __name__ == "__main__":
    main()
