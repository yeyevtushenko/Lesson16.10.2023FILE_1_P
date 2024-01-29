def divide_numbers():
    try:
        numerator = float(input("Введіть чисельник: "))
        denominator = float(input("Введіть знаменник: "))

        result = numerator / denominator
        print(f"Результат ділення: {result}")

    except ValueError:
        print("Помилка: Введено неправильний формат числа.")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе.")


if __name__ == "__main__":
    divide_numbers()