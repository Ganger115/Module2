numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] #Простое числа (числа, которое делится только на 1 и на себя).
not_primes = [] #Не простые числа

for elem in numbers:
    Flag = True
    for divisor in range(2, elem):
        if elem % divisor == 0:
            Flag = False
            not_primes.append(elem)
            break
    if Flag == True and elem != 1:
        primes.append(elem)

print("Primes:", primes)
print("Not primes:", not_primes)
