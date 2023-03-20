# Найдите сумму цифр трехзначного числа.

a = int (input ("Введите трехзначное число: "))
print (a)
digit1 = a %10
a = a//10
digit2 = a % 10
a = a//10
print ("Сумма чисел = ", a + digit2 + digit1)