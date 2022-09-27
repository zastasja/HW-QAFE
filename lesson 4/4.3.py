# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
# создайте новый список, содержащий только положительные числа

my_list = [20, -3, 15, 2, -1, -21]
def positive(lst, filter=None):
    if filter is None:
        return lst

    r = []
    for x in lst:
        if filter(x):
            r.append(x)

    return r

res = positive(my_list, lambda x: x > 0)
print(res)