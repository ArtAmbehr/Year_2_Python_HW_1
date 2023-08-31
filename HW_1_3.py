# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу 
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Введите число: "))

if num < 0 or num > 100000:
    print("Число должно быть положительным и не превышать 100000")
elif num == 1:
    print("Число не является ни простым, ни составным")
else:
    is_prime = True
for i in range(2, int(num/2) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("Число является простым")
else:
    print("Число является составным")
