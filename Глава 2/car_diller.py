car_price = int(input('Введите стоимость автомобиля без наценок: '))
car_tax = car_price * 0.2
reg_duty = car_price * 0.1
agency_duty = 2000
delivery_price = 500
last_cat_price = car_price + car_tax + reg_duty + agency_duty + delivery_price
print(last_cat_price)