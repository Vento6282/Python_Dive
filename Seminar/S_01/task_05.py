# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n, e = 10, 3
i, sum = 1, 0
while i <= n:
    if i % 2 == 0 and i % e != 0:
        print(i)
        sum = sum + i
    i = i + 1
print(f'Сумма четных элеменетов от 1 до {n}, исключая числа кратные {e} - {sum}')