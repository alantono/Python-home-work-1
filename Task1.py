# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
day = int(input('Введите цифру означающую день недели (от 1 до 7): '))
if (day == 6 or day == 7):
    print(day, '-> да')
else:
    print(day, '-> нет')