print('Задача 7. Банкомат')

# Пользователи банкомата хотят снимать деньги.
# Но банкомат умеет выдавать только купюры по 100 рублей.
# Напишите программу,
# которая проверяет допустимость суммы средств, которую ввёл пользователь.
 
# Пример:
# Введите сумму, которую хотите снять: 250
# Такую сумму снять невозможно. Обратитесь в другой банкомат.

print("Банкомат умеет выдавать только купюры по 100 рублей.")
bankomat_sum = int(input("Введите сумму, которую хотите снять: "))
if bankomat_sum % 100 == 0:
    print("Купюры выдаются: ", bankomat_sum)  
else: 
    print("Такую сумму снять невозможно. Обратитесь в другой банкомат.")
    