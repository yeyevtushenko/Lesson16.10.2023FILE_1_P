def convert_to_number(string):
    try:
        number = float(string)
        return number
    except ValueError:
        try:
            number = float(string.capitalize())
            return number
        except ValueError:
            raise ValueError("Помилка: Неможливо перетворити рядок на число.")


input_string = input("Введіть рядок для перетворення на число: ")

try:
    result = convert_to_number(input_string)
    print(f"Результат перетворення: {result}")
except ValueError as e:
    print(e)