num = input("Number:")
num = num[::-1]
name = input("Name")
accName = list(name)
acc = list(num)
acc.extend(accName)
k = 0

for i in range(len(acc)):
    if i % 2 == 0:
        if acc[i] == '0':
            acc[i] == '9'

        elif acc[i] == 'a':
            acc[i] = 'z'

        elif acc[i] == 'A':
            acc[i] = 'Z'

        else:
            k = ord(acc[i])
            k = k - 1
            acc[i] = chr(k)


    else:
        if acc[i] == '9':
            acc[i] == '0'

        elif acc[i] == 'z':
            acc[i] = 'a'

        elif acc[i] == 'Z':
            acc[i] = 'A'

        else:
            k = ord(acc[i])
            k = k + 1
            acc[i] = chr(k)

print(''.join(acc))
