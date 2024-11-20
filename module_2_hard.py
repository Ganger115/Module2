import random
number = random.randint(3, 20)
couples = []
list_coup = []

for x in range(1, number):
    for y in range(1, number):
        if all([number % (x + y) == 0, x != y, [y, x] not in couples]):
            couples.append([x,y])
for i in couples:
    list_coup.extend(i)

cipher = ''.join(str(x) for x in list_coup)

print(number, '-', cipher)