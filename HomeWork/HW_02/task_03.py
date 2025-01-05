# Программа принимает целое число и возвращает его римское представление в виде строки.



number = 871

number_str = ''
length_number = len(str(number))
for i in range(length_number):
    temp = ((number % (pow(10,length_number - i))) // (pow(10,length_number - 1 - i)))
    print(temp)
    temp = ((number % (pow(10,length_number - i))) // (pow(10,length_number - 1 - i)) * (pow(10,length_number - 1 - i)))


    print(temp)
