a = list(range(1, 10))
b = 1
tabl = []
while b != 10:
    i = 1
    while i != 9:
        c = b * i
        tabl.append(f'{b} * {a[i]} = {c}')
        i += 1
    else:
        b += 1
for elem in range(len(tabl)):
    print(tabl[elem])

# Другое решение
# a = list(range(1,10))
# b = 1
# while b != 10:
#    i = 1
#    while i !=9:
#        c = b * a[i]
#        print(f'{b} * {a[i]} = {c}')
#        i = i + 1
#    else :
#        b = b + 1
