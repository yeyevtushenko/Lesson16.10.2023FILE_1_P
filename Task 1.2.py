def divide_numbers_version1(numerator, denominator):
    result = numerator / denominator
    return result


def divide_numbers_version2(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе.")
        return None


if __name__ == "__main__":
    try:
        numerator_input = float(input("Введіть чисельник: "))
        denominator_input = float(input("Введіть знаменник: "))

        result_output_version1 = divide_numbers_version1(numerator_input, denominator_input)
        print(f"Результат версії 1: {result_output_version1}")

        result_output_version2 = divide_numbers_version2(numerator_input, denominator_input)

        if result_output_version2 is not None:
            print(f"Результат версії 2: {result_output_version2}")

    except ValueError:
        print("Помилка: Введено неправильний формат числа.")
