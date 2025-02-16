# ##################### НАСТРОЙКИ ОКРУЖЕНИЯ #####################
import struct
import time
import math
from datetime import datetime
import matplotlib.pyplot as plt

# ##################### ГЕНЕРАТОР ПСЕВДОСЛУЧАЙНЫХ ЧИСЕЛ #####################

# параметры для формулы ci = (a*ci-1+ b) (mod m)
def formula_parameters():
    n = 24
    m = 2 ** n
    return n, m

# Текущая микросекунда
def microsecond():
    return datetime.now().microsecond

# Текущий час
def hour():
    return datetime.now().hour

# Текущий день
def day():
    return datetime.now().day

# Текущий месяц
def month():
    return datetime.now().month

# Текущий год
def year():
    return datetime.now().year

# Получение случайных a и b и с
def generate_abc():

    n, m = formula_parameters()

    # Параметр a. От времени суток, остаток.
    a = math.ceil(microsecond() / math.ceil(math.sqrt(day() / 57))) + \
        math.ceil(day() / math.ceil(year() * month())) + \
        math.ceil(34 / (7 + microsecond() % 24)) - year() * month()
    while a % 6 != 1:
        a += 1

    # Параметр b. От времени суток, остаток, НОД.
    b = year() * month() + 5 * \
        math.ceil(microsecond() / 104) + \
        math.ceil(31 / (12 + microsecond() % 14)) - year() * month()
    while b % 2 != 1 and math.gcd(b, m) != 1:
        b += 1

    # Параметр c. От времени суток.
    c = math.ceil(microsecond() / (hour() + 22)) + math.ceil(year() * (hour() + 3)) + \
        math.ceil(math.sqrt(day() / 43)) + \
        math.ceil(71 / (22 + microsecond() % 24)) + year() * month()

    # Вывод значений
    print("Значения ключей:", "\na =", a, "\nb =", b, "\nc =", c)

    return a, b, c


# ГПСЧ. Возвращает список или одно число. ci = (a*ci-1+ b) (mod m)
def linear_congruent_generator(a, b, c, sequence_length):

    n, m = formula_parameters()
    
    # degree_of_two = (microsecond() + day()) % 24
    degree_of_two = n

    # Последовательность длины 1 (ограничение сверху 4096)
    if sequence_length == 1:
        return [math.ceil((a * c + b) % 2**degree_of_two) % 255]

    # Массив символов исходного сообщения
    sequence_result = [0 for i in range(sequence_length + 1)]
    sequence_result[0] = math.ceil(c)

    for i in range(1, sequence_length + 1):
        sequence_result[i] = math.ceil((a * sequence_result[i-1] + b) % 2**degree_of_two) % 255

    # массив числовых представлений символов
    return sequence_result[1:sequence_length + 1]

# ##################### ШИФРОВАНИЕ #####################

# Гаммирования текста по ключу
def encrypt(text):
    # Место сохранения
    save_path = input("Введите название, под которым сохранить зашифрованное сообщение в формате {название}.txt: ")
    file_message = open(save_path, 'w', encoding="utf-8")
    message = ""

    # Получаем ключи
    key_path = input("Введите название файла-ключа (в формате {название}.key): ")
    file_keys = open(key_path, 'r', encoding="utf-8")
    keys = file_keys.read()
    file_keys.close()

    a, b, c = keys.split(" ")

    key = linear_congruent_generator(int(a), int(b), int(c), len(text))

    # Запуск секундомера
    time_start = time.time()

    # Гаммирование
    for i in range(len(text)):
        # ord = число символа Unicode. ^ = XOR
        simvol = ord(text[i]) ^ int(key[i]) 
        # chr = число в символ Unicode
        message += chr(simvol)

    # Остановка секундомера
    time_stop = time.time()

    print("Время выполнения программы составляет: ", time_stop - time_start)
    file_message.write(message)
    file_message.close()


# ##################### ИНТЕРФЕЙС ПОЛЬЗОВАТЕЛЯ #####################

def main():

    text = None

    while True:
        user_select = int(input(
            "Выберите режим:\n" + 
            "(1): Сгенерировать и записать в файл ключ\n" + 
            "(2): Зашифровать/дешифровать файл\n" + 
            "(3): Выход\n" + 
            "Ваш выбор: "))

        if user_select == 1:
            # Сгенирировать параметры a, b, c
            a, b, c = generate_abc()

            # записать ключ в файл
            key_path = input("Введите название, под которым сохранить файл-ключей (в формате {название}.key): ")
            file = open(key_path, 'w', encoding="utf-8")
            file.write(str(a) + ' ' + str(b) + " " + str(c))
            file.close()            

        elif user_select == 2:
            try:
                # Получить файл
                save_path = input("Введите путь до файла с текстом (в формате {название}.txt): ")
                file = open(save_path, "r", encoding="utf-8")
                text = file.read()
                file.close()

                # Зашифровать / расшифровать файл
                encrypt(text)
            except:
                print("В начале необходимо сгенерировать и записать в файл ключ!")

        elif user_select == 3:
            # Выход
            exit(0)


# ##################### ЗАПУСК ПРОГРАММЫ #####################

if __name__ == "__main__":
    main()
