from datetime import datetime
from pprint import pprint


def time(old_function):
    """
    Декоратор
    :param old_function:
    :return: Он записывает в файл дату и время вызова функции,
    имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
    """

    def wrap(*args, **kwargs):
        print(f'Function {old_function.__name__} was called')
        print(f'Arguments: {args}')
        result = old_function(*args, **kwargs)
        print(f'{result} was returned')
        print(f'Date = {datetime.now()}')
        with open('text', 'w') as f:
            f.write(f'Function {old_function.__name__} was called\n')
            f.write(f'{result} was returned\n')
            f.write(f'Date = {datetime.now()}\n')
            f.write(f'Arguments: {args}\n')
        return result

    return wrap


def time1(path):
    def _time(old_function):
        def wrap(*args, **kwargs):
            print(f'Function {old_function.__name__} was called')
            print(f'Arguments: {args}')
            result = old_function(*args, **kwargs)
            print(f'{result} was returned')
            print(f'Date = {datetime.now()}')
            with open('text', 'w') as f:
                f.write(f'Function {old_function.__name__} was called\n')
                f.write(f'{result} was returned\n')
                f.write(f'Date = {datetime.now()}\n')
                f.write(f'Arguments: {args}\n')
            return result

        return wrap
    return _time


@time1(r'C:\Users\Пользователь\PycharmProjects\Netology\decorators\text')
def gen(value1, value2):
    x = [x ** 2 for x in range(value1, value2) if x % 2 == 0]
    return x
print(gen(10, 20))
