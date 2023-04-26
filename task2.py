# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random

def getarray(min,max, n): # составляет список 
    arr = []
    for i in range(n):
        arr.append(random.randint(min,max))
    return arr

def arrIndex(array,min,max): # ищет индексы в заданном диапазоне 
    indexes = []
    for i,j in enumerate(array):
        if j >=min and j <=max:
            indexes.append(i)
    return indexes

n = int(input("Введите длину массива: "))
newarray = getarray(-20,20,n)
print(newarray)
print(arrIndex(newarray,5,16)) # Диапазон от 5 до 15 
