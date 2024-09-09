# Модуль обработки регулярных выражений
import re

# Создание функции поиска чисел строках.
def calculate_structure_sum(data_structure):

    def extract_numbers_from_string(s):
        # Поиск цифровых последовательностей в строке.
        matches = re.findall(r'\d+', s)
        # Преобразование всех найденных цифровых строк в целые числа.
        return [int(match) for match in matches]

    # Функция суммирования длин строк и чисел.
    def recursive_sum(structure):
        # Переменная суммирования.
        total = 0

        # Задание начального условия типа данных (список, кортеж, множества):
        if isinstance(structure, (list, tuple, set)):
            # Создание цикла для перебора всех элементов данных.
            for item in structure:
                # Увеличение переменной суммирования на
                # полученный результат функции для каждого элемента.
                total += recursive_sum(item)

        # Если тип данных - словарь:
        elif isinstance(structure, dict):
            # Цикл для всех ключей словаря с их значениями:
            for key, value in structure.items():
                # Увеличение переменной на сумму длины ключа
                # и его значения с рекурсивным вызовом функции.
                total += recursive_sum(key) + recursive_sum(value)

        # Если тип данных строка:
        elif isinstance(structure, str):
            # Увеличиваем переменную на длину строки.
            total += len(structure)
            # Увеличиваем переменную на сумму чисел, найденных в строке.
            total += sum(extract_numbers_from_string(structure))

        # Если тип данных целое число или с плавающей запятой:
        elif isinstance(structure, (int, float)):
            # Увеличиваем переменную на данное число.
            total += structure

        # Возвращение переменной.
        return total

    # Возвращение результата функции.
    return recursive_sum(data_structure)

# Ввод данных.
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Окончательный результат.
result = calculate_structure_sum(data_structure)
# Вывод результата.
print(result)