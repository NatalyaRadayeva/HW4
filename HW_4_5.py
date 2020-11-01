# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()


from functools import reduce

my_list = []

for item in range(100, 1001):
    if(item % 2) == 0:
        my_list.append(item)
print(my_list)

result = reduce(lambda x, y: x*y, my_list)
print(result)