per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую планируете положить под проценты: "))

deposit = []

for value in per_cent.values():
    dep = round(value * money / 100)
    deposit.append(dep)

print("Максимальная сумма, которую вы можете заработать —", max(deposit))