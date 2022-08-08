num_range = range(0,10,2)
#for i in num_range:
    #print(i)

def ask_number(low = 0, high = 100, multiple = 1):
    response = None
    while response not in range(low,high,multiple):
        response = int(input('Введите число'))
        multiple = int(input('Введите шаг(кратность): '))
    return print('Число', response, "в списке с шагом(кратностью)", multiple)

ask_number()