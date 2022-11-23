# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not

list = [0, 1]
for i in list:
    x = i
    y = i
    z = i
    for j in list:
        y = j
        z = j
        for k in list:
            z = k
            print(x, y, z)
if not (x or y or z) == (not x and not y and not z):
    print('true')
else:
    print('false')
