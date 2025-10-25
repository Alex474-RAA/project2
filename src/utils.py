import json
import logging
import os
from datetime import datetime
from typing import Dict, List

# Создаем папку logs если её нет
os.makedirs("logs", exist_ok=True)

# Создаем отдельный объект логера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Уровень не меньше DEBUG

# Настраиваем file_handler для логера модуля utils
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Настраиваем file_formatter для логера модуля utils
# Формат включает метку времени, название модуля, уровень серьезности и сообщение
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Устанавливаем форматер для логера модуля utils
file_handler.setFormatter(file_formatter)

# Добавляем handler для логера модуля utils
logger.addHandler(file_handler)


def get_date(date_iso: str) -> str:
    """
    Принимает на вход строку с датой в формате ISO.
    Возвращает строку с датой в формате "ДД.ММ.ГГГГ".

    :param date_iso: Строка с датой в формате ISO.
    :return: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    try:
        date = datetime.fromisoformat(date_iso)
        result = date.strftime("%d.%m.%Y")
        # Логирование успешного случая
        logger.info(f"Успешное преобразование даты: {date_iso} -> {result}")
        return result
    except Exception as e:
        # Логирование ошибочного случая с уровнем не ниже ERROR
        logger.error(f"Ошибка преобразования даты {date_iso}: {type(e).__name__} - {str(e)}")
        raise


def load_json_data(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список в случае ошибки.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что данные являются списком
            if isinstance(data, list):
                # Логирование успешного случая
                logger.info(f"Успешно загружено {len(data)} транзакций из файла {file_path}")
                return data
            else:
                logger.warning(
                    f"Данные в файле {file_path} не являются списком, "
                    f"возвращен пустой список"
                )
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Логирование ошибочного случая с уровнем не ниже ERROR
        logger.error(f"Ошибка загрузки данных из файла {file_path}: {type(e).__name__} - {str(e)}")
        return []
