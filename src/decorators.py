import functools


from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций и их результатов.

    Args:
        filename (str, optional): Имя файла для записи логов.
        Если не указано, логи выводятся в консоль.

    Returns:
        function: Декорированная функция с логированием.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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


def write_log(message: str, filename: Optional[str] = None) -> None:
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
