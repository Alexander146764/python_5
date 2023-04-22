#  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 


number = int(input("Введите число : "))
a = number
degree_value = int(input("Введите степень : "))
b = degree_value
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

print(a, "в степени", b, "=", power(a, b))


