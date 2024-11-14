my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
name = 0
print("Исходные данные:", "\nmy_list =", my_list)
print("Вывод на консоль:")
while name < len(my_list):
    num = my_list[name]
    name += 1
    if num == 0:
        continue
    elif num < 0:
        break
    elif name == len(my_list):
        print(num)
    else:
        print(num)