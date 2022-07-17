__author__ = "Чеканов Вячеслав Александрович"
# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
lst = ["яблоко", "банан", "киви", "арбуз"]
maxlen = 0
for i in lst:
    if len(i) > maxlen:
        maxlen = len(i)
for i in range(len(lst)):
    print(("{0}. {1:>" + str(maxlen) + "}").format(i + 1, lst[i]))
print()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.

lst1 = [1, 3, 5, 7, 9]
lst2 = [3, 8, 6, 5]
res = []
print(lst1, lst2)
for i in lst1:
    if i not in lst2:
        res.append(i)
lst1 = res
print(lst1, lst2)
print()


# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lst = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]
res = []
print(lst)
for i in lst:
    if i % 2 == 0:
        res.append(int(i / 4))
    else:
        res.append(i * 2)
print(res)

# вариант 2
def prepare(item):
    return int(item / 4) if item % 2 == 0 else item * 2

res2 = list(map(prepare, lst))
print(res2)


