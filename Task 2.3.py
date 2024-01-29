def display_menu():
    print("\nМеню:")
    print("1. Відображення словника")
    print("2. Пошук значення в словнику")
    print("3. Заміна значення в словнику")
    print("4. Відображення значення за ключем")
    print("5. Видалення значення за ключем")
    print("0. Вихід")


def display_dictionary(dictionary):
    print("\nСловник:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")


def search_value(dictionary, key):
    try:
        value = dictionary[key]
        print(f"Значення для ключа {key}: {value}")
    except KeyError:
        print(f"Помилка: Ключ {key} відсутній у словнику.")


def replace_value(dictionary, key, new_value):
    try:
        dictionary[key] = new_value
        print(f"Значення за ключем {key} замінено на {new_value}")
    except KeyError:
        print(f"Помилка: Ключ {key} відсутній у словнику.")


def main():
    user_dictionary = {}

    while True:
        display_menu()

        try:
            choice = int(input("Виберіть опцію: "))
        except ValueError:
            print("Помилка.")
            continue

        if choice == 1:
            display_dictionary(user_dictionary)
        elif choice == 2:
            key_to_search = input("Введіть ключ для пошуку: ")
            search_value(user_dictionary, key_to_search)
        elif choice == 3:
            key_to_replace = input("Введіть ключ для заміни значення: ")
            new_value = input("Введіть нове значення: ")
            replace_value(user_dictionary, key_to_replace, new_value)
        elif choice == 4:
            key_to_display = input("Введіть ключ для відображення значення: ")
            search_value(user_dictionary, key_to_display)
        elif choice == 5:
            key_to_delete = input("Введіть ключ для видалення значення: ")
            try:
                del user_dictionary[key_to_delete]
                print(f"Значення за ключем {key_to_delete} видалено")
            except KeyError:
                print(f"Помилка: Ключ {key_to_delete} відсутній у словнику.")
        elif choice == 0:
            print("Програма завершена.")
            break
        else:
            print("Помилка")


if __name__ == "__main__":
    main()