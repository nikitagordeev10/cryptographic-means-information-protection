# Импорт библиотек
from email import message
import sys

# Проверка, что значение не привосходит размер
def CheckLess(string_key, limit):
    return (all(x <= limit for x in string_key))

# Проверка уникальности значений списка
def CheckUniqueObjects(input_list):
    unique_input_set = set(input_list)
    unique_out_list = list(unique_input_set)
    if (len(unique_out_list) == len(input_list)):
        return True
    else:
        return False

# Комплексная проверка значений списка
def CheckListValues(check_list, limit):
    if (type(check_list) == list and len(check_list) == limit and CheckLess(check_list, limit) and CheckUniqueObjects(check_list)):
        print("Ключи введены верно")
    else:
        sys.exit("Ключи введены не верно")

# Дозаполнение сообщения пробелами до размера кратного 4м
def FillMessage(input_message):
    if (len(input_message) % 4 == 0):
        return input_message
    else:
        input_message += ' ' * (4 - len(input_message) % 4)
        return input_message

# Определение позиции для заполнения матрицы
def DefinePosition(i, division):
    return (i//division + 1)
