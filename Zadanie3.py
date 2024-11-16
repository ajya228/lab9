#Имеется файл с данными в формате csv:Продукт,Количество,Цена
#Молоко,2,80
#Сыр,1,500
#Хлеб,2,70
# Напишите программу, которая считывает данные из этого файла, подсчитывает итоговую сумму расходов и выводит данные в виде:
# Нужно купить:
# Молоко - 2 шт. за 80 руб.
# Сыр - 1 шт. за 500 руб.
# Хлеб - 2 шт. за 70 руб.
# Итоговая сумма: 800 руб.
list: dict = {}
with open('table_laba.csv', encoding = 'utf' ) as f:
    data = f.readlines()  # data - list[str]
    data.pop(0)
    for item in data:
        item = item.split(',')
        list[item[0]] = {'количество': int(item[1]), 'цена': int(item[2])}
print(list)

print('Нужно купить: \n')
price = 0
for product in list:
    price += list[product]['цена'] * list[product]['количество']
    print(f'{product} — {list[product]["количество"]} шт. за {list[product]["цена"]} руб.')
print(f'\nОбщая сумма: {price} руб.')