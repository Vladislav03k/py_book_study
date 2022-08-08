# Программа считает последовательность которую задает пользователь от начала и до конца, с заданным интервалом

start = int(input('Введите начала отсчета: '))
stop = int(input('Введите конец отсчета: '))
interval = int(input("Введите необходимый интервал: "))
for number in range(start, stop + 1, interval):
    print(number)