#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#5
#1 2 3 4 5
#6
#-> 5

N = int(input('Введите размер массиве: '))
A = input("Введите элементы массива: ")
A_n = list(map(int, A))
X = int(input('Введите число X: '))
min = (X - A_n[0])
index = 0
for i in range(1, N):
    count = (X - A_n[i])
    if count < min:
        min = count
        index = i
print(f' наиболее близкое число {A_n[index]}')