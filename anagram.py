a = input("Enter String 1:")
b = input("enter String 2:")
a = a.lower()
b = b.lower()
k = list(a)
l = list(b)

def spacRemov(x):
    for i in x:
        if i == ' ':
            del x[x.index(i)]

spacRemov(k)
spacRemov(l)

k.sort()
l.sort()

if k == l:
    print(f"{b} is an anagram of {a}")
else:
    print("Not anagrams")
