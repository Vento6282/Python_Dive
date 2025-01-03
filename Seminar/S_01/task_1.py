# Работа в консоли в режиме интерпретатора Python.
# Решите квадратное уравнение 5x2-10x-400=0 последовательно сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c.

from math import  sqrt

a, b, c = 5, -10, -400
d = (b**2) - (4 * a * c)
if (d > 0):
    x1 = (- b + sqrt(d)) / (2 * a)
    x2 = (- b - sqrt(d)) / (2 * a)
    print (f'Корни уравнениея - {x1, x2}')
elif (d == 0):
    x1 = - b / 2 * a
    print (f'Корень уравнениея - {x1}')
elif (d < 0):
    print('Корней нет!')