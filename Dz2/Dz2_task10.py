# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


total = int(input('Введите кол-во монет: '))
coins = []
for i in range(total):
    coin = int(input(f'{i+1}: '))
    coins.append(coin)
print(coins)

min_try= 0
for i in coins:
    if i > 0:
        min_try += 1
print(min_try if min_try < len(coins)/2 else len(coins) - min_try)
