# =========================== РУССКИЙ АЛФАВИТ ===========================
# https://planetcalc.ru/1434/

# =========================== ДРУГОЙ АЛФАВИТ ===========================
message = "ЖГБФЖ"
res = []
alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

for key in range(1, 33):
    for i in range(len(message)):
        res.append(alfavit[(alfavit.find(message[i])+key)%len(alfavit)])
    print(key,"".join(res))
    res = []