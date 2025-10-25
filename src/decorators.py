import functools
import logging
import os
from typing import Any, Callable, Optional

# Создаем папку logs если её нет
os.makedirs("logs", exist_ok=True)

# Настройка логера для декораторов
logger = logging.getLogger("decorators")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/decorators.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
                error_message = (f"{func.__name__} error: {type(e).__name__}. "
                                 f"Inputs: {args}, {kwargs}")
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
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
