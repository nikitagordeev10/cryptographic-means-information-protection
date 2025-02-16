alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
n = 34
key = "БОЯРЫШНИК"
mes = "ОФЁВАКУЛЪЛОЬЬЛЩЬ"
res = ""

for i in range(len(mes)):
    z = (alf.find(mes[i]) + alf.find(key[i % len(key)])) % n + 1
    res += alf[z % n]

print(res)

# dencrypt

res = ""

for i in range(len(mes)):
    z = (alf.find(mes[i]) - alf.find(key[i % len(key)])) % n - 1
    res += alf[z % n]

print(res)