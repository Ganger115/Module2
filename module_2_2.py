print("Ввод в консоль 1:") #Первая консоль

first = input()
second = input()
third  = input()

if first == second and second == third:
    print("Вывод на консоль 1:", """
3""")
elif first == second or second == third or first == third:
    print("Вывод на консоль 1:", """
2""")
else:
    print("Вывод на консоль 1:", """
0""")

print("""
Ввод в консоль 2:""") #Вторая консоль

first = input()
second = input()
third = input()

if first == second and second == third:
    print("Вывод на консоль 2:", """
3""")
elif first == second or second == third or first == third:
    print("Вывод на консоль 2:", """
2""")
else:
    print("Вывод на консоль 2:", """
0""")
