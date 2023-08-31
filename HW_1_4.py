# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:

# from random import
# randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

for attempt in range(attempts):
    guess = int(input("Угадайте число от 0 до 1000: "))
    if guess < num:
        print("Число больше")
    elif guess > num:
        print("Число меньше")
    else:
        print("Вы угадали!")
        break
if guess != num:
    print(f"Вы не угадали. Загаданное число было: {num}")

