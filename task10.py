print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 

first_dig = int(input("Введите первое число: "))
second_dig = int(input("Введите второе число: "))
third_dig = int(input("Введите третье число: "))

### Решение номер 1
#temp_dig = first_dig
#if temp_dig < second_dig:
#     temp_dig = second_dig
#if temp_dig < third_dig:
#     temp_dig = third_dig
#print("Максимальное число", temp_dig)


### Решение номер 2
l=[]
l.append(first_dig)
#print(l)
l.append(second_dig)
#print(l)
l.append(third_dig)
#print(l)

print(max(l))

