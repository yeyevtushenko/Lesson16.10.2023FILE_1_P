import math


def calculate_square_root_v1(number):
    return math.sqrt(number)


def calculate_square_root_v2(number):
    if number < 0:
        raise ValueError("Негативне число не має квадратного кореня")
    return math.sqrt(number)


try:
    user_input = float(input("Введіть число для обчислення квадратного кореня: "))
    result = calculate_square_root_v1(user_input)
    print(f"Квадратний корінь з числа {user_input} дорівнює {result}")
except ValueError as ve:
    print(f"Помилка: {ve}")

try:
    user_input = float(input("Введіть число для обчислення квадратного кореня: "))
    result = calculate_square_root_v2(user_input)
    print(f"Квадратний корінь з числа {user_input} дорівнює {result}")
except ValueError as ve:
    print(f"Помилка: {ve}")