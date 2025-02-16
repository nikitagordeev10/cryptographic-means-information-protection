key = input("Ключ: ")
message = input("Сообщение: ")
todo = int(input("0 - зашифровать, 1 - расшифровать: "))

encrypted = ""
decrypt = [''] * len(message)
step = len(key)
i = 0
j = step

while j <= len(message):
    messageSlice = message[i:j]
    print(messageSlice)
    if todo == 0:
        for p in key:
            encrypted += messageSlice[int(p) - 1]
    else:
        c = 0
        for p in key:
            decrypt[i + int(p) - 1] = messageSlice[c]
            c += 1
    i += step
    j += step

leftSymbols = len(message) % len(key)

if leftSymbols != 0:
    messageSlice = message[i:i + leftSymbols]
    if todo == 0:
        for p in key:
            if int(p) > leftSymbols:
                continue
            encrypted += messageSlice[int(p) - 1]
    else:
        c = 0
        for p in key:
            if int(p) > leftSymbols:
                continue
            decrypt[i + int(p) - 1] = messageSlice[c]
            c += 1

if todo == 0:
    print(encrypted)
else:
    print(''.join(decrypt))
