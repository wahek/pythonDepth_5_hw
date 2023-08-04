def ex_1(path_all: str) -> tuple:
    """Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""
    *path, name = path_all.split('\\')
    name, extension = name.split('.')
    return path, name, extension


def ex_2(first: list, second: list, third: list) -> dict:
    """Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
    ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве
    ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии"""
    return {name: salary * float(percent) / 100 for name, salary, percent in
            zip(first, second, map(lambda x: x[:-1], third))}


def ex_3():
    """Создайте функцию генератор чисел Фибоначчи (см. Википедию)"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


print(ex_1(r'D:\Games\The Witcher 3 Wild Hunt\bin\x64\witcher3.exe'))
print('\n')
print(ex_2(['vv', 'nn'], [1234, 3456], ['12%', '5.5%']))
fib_gen = ex_3()
for i in range(int(input('Сколько чисел сгенерировать: '))):
    print(next(fib_gen))
