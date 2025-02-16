alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
key = "ЧЕРНИКА"
message = "ЖЙУЦЪЭРЧЫЩЛЗЬОШ_ВЦТ"
res = ""

# =========================== КВАДРАТ ВИЖЕНЕРА ===========================
a = []
for i in range(len(alf)):
    a.append([])
    for j in range(len(alf)):
        n = (j + i) % len(alf)
        a[i].append(alf[n])


# =========================== ШИФРОВАНИЕ ===========================
# for i in range(len(message)):
#     y1 = a[0].index(message[i])
#     y2 = a[0].index(key[i % len(key)]) 
#     res += a[y1][y2]

# =========================== РАСШИФРОВКА ===========================
for i in range(len(message)):
    y2 = a[0].index(key[i % len(key)]) 
    y1 = a[y2].index(message[i])
    res += a[0][y1]

# =========================== РЕЗУЛЬТАТ ===========================
print(res)