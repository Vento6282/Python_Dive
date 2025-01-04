# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def type(number):
    if number >= 1 and number <=9:
        return (f'{number} - цифра. Квадрат {number} = {sqrt(number)}')
    elif number >= 10 and number <=99:
        return (f'{number} - двузначное число. Произведение цифр {number} = {multi(number)}')
    elif number >= 100 and number <=999:
        return (f'{number} - трёхзначное число. Зеркальное отображение {number} = {mirror(number)}')

def sqrt(number):
    return number ** 2

def multi(number):
    return (number // 10) * (number % 10)

def mirror(number):
    return (number % 10 * 100) + (number // 10 % 10 * 10) + (number // 100)

print(type(5))
print(type(55))
print(type(123))