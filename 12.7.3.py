per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму взноса:"))
deposit = []
deposit.append(money*per_cent['ТКБ'])
deposit.append(money*per_cent['СКБ'])
deposit.append(money*per_cent['ВТБ'])
deposit.append(money*per_cent['СБЕР'])
print("Максимальная сумма после взноса, составляет:", max(deposit))