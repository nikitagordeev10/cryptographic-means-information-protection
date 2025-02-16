alf = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
message = "КЫХЛЖЕЗИРШДНЯИПОАТЖВ"
key = "МАЛИНА"
result = ""

# ====================== КОД АЛФАВИТА ======================
alf_num = []
for i in range(len(alf)):
    alf_num.append(bin(i)[2:].zfill(5))

# ОБЪДИНЕНИЕ ДВОИЧНОГО КОДА ОТКРЫТОГО ТЕКСТА С ДВОИЧНЫМ КОДОМ КЛЮЧА
for i in range(len(message)):
    word = alf_num[alf.index(message[i])]
    key_num = alf_num[alf.index(key[i % len(key)])]
    res = ""

    # Исключающие ИЛИ
    for i in range(len(word)):
        res += str(int(word[i]) ^ int(key_num[i]))
    
    n = alf_num.index(res)
    result += alf[n]

print(result)
    
