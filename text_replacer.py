def replace_in_file(input_file, output_file, search_str, replace_str):
    try:
        # Чтение файла
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Замена строки
        new_content = content.replace(search_str, replace_str)

        # Запись в новый файл
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Файл успешно сохранён как {output_file}")
        print("test")

    except FileNotFoundError:
        print("Ошибка: файл не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
#
if __name__ == "__main__":
    input_file = "input.txt"  # Имя исходного файла
    output_file = "output.txt"  # Имя нового файла
    search_str = "старая_строка"  # Строка для поиска
    replace_str = "новая_строка"  # Строка для замены

    replace_in_file(input_file, output_file, search_str, replace_str)