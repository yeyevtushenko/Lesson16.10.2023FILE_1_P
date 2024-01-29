import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Введіть додатнє число для обчислення квадратного кореня.")
    return math.sqrt(number)

try:
    user_input = float(input("Введіть число для обчислення квадратного кореня: "))
    result = calculate_square_root(user_input)
    print(f"Квадратний корінь з {user_input} дорівнює {result:.2f}")
except ValueError as ve:
    print(f"Помилка: {ve}")
except Exception as e:
    print(f"Виникла невідома помилка: {e}")

