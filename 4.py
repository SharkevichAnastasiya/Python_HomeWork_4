#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n – кол – во элементов первого  множества. m – кол – во элементов второго множества.
#Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение).


# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# myset_1 = set()
# myset_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     myset_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     myset_2.add(i)
# lok = myset_1 & myset_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')




#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
#Она растет на круглой грядке, причем кусты высажены только по окружности.
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i- ом кусте
#выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#Эта система состоит из управляющего модуля нескольких собирающих модулей. Собирающий модуль за один заход, находясь
#непосредственно перед кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
#находясь перед некоторым кустом заданной во входном файле грядки.


# n = int(input())
# arr = list()
# for i in range(n):
#     x = int(input())
#     arr.append(x)

# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(max(arr_count))