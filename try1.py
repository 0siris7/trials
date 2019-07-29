
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1

        else:
            d[c] += 1
    return d



k = histogram('parrot')

dict2 = dict()

for key in k:
    val = k[key]
    if val not in dict2:
        dict2[val] = [key]
    else:
        dict2[val].append(key)

print(dict2)
