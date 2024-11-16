console_output = "Вывод на консоль 1:"
print("Ввод в консоль 1:")

first = input()
second = input()
third  = input()

if first == second and second == third:
    print(console_output, "\n3")
elif first == second or second == third or first == third:
    print(console_output, "\n2")
else:
    print(console_output, "\n0")
