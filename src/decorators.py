import functools


def log(filename=None):
    """
    Декоратор для логирования вызовов функций и их результатов.

    Args:
        filename (str, optional): Имя файла для записи логов.
        Если не указано, логи выводятся в консоль.

    Returns:
        function: Декорированная функция с логированием.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                write_log(message, filename)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                write_log(error_message, filename)
                raise e

        return wrapper

    return decorator


def write_log(message, filename=None):
    """
    Записывает сообщение в файл или выводит в консоль.

    Args:
        message (str): Сообщение для записи.
        filename (str, optional): Имя файла. Если None, вывод в консоль.
    """
    if filename:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    else:
        print(message)
