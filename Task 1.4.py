def string_to_number(input_str):
    return int(input_str)


def version_without_exception_handling():
    user_input = input("Введіть рядок для перетворення на число: ")
    try:
        result = string_to_number(user_input)
        print(f"Числове представлення рядка: {result}")
    except ValueError:
        print("Помилка: Неможливо перетворити рядок на число.")


def version_with_exception_handling():
    user_input = input("Введіть рядок для перетворення на число: ")
    result = None
    try:
        result = string_to_number(user_input)
    except ValueError:
        print("Помилка: Неможливо перетворити рядок на число.")
    if result is not None:
        print(f"Числове представлення рядка: {result}")


print("Версія без обробки винятку усередині функції:")
version_without_exception_handling()

print("\nВерсія з обробкою винятку усередині функції:")
version_with_exception_handling()