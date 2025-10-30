import logging
import os
from typing import Dict, List

import pandas as pd

# Настройка логера для модуля file_reader
logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)

# Создаем папку logs если её нет
os.makedirs("logs", exist_ok=True)

file_handler = logging.FileHandler("logs/file_reader.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv_file(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу с транзакциями

    Returns:
        List[Dict]: Список словарей с данными о транзакциях

    Raises:
        Exception: Если файл не найден или произошла ошибка чтения
    """
    try:
        logger.info(f"Начало чтения CSV файла: {file_path}")

        # Проверяем существование файла
        if not os.path.exists(file_path):
            error_msg = f"CSV файл не найден: {file_path}"
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        # Читаем CSV файл
        df = pd.read_csv(file_path)

        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict("records")

        logger.info(f"Успешно прочитано {len(transactions)} транзакций из CSV")
        return transactions

    except Exception as e:
        error_msg = f"Ошибка чтения CSV файла {file_path}: {str(e)}"
        logger.error(error_msg)
        raise  # Просто перебрасываем оригинальное исключение


def read_excel_file(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу с транзакциями

    Returns:
        List[Dict]: Список словарей с данными о транзакциях

    Raises:
        Exception: Если файл не найден или произошла ошибка чтения
    """
    try:
        logger.info(f"Начало чтения Excel файла: {file_path}")

        # Проверяем существование файла
        if not os.path.exists(file_path):
            error_msg = f"Excel файл не найден: {file_path}"
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        # Читаем Excel файл
        df = pd.read_excel(file_path)

        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict("records")

        logger.info(f"Успешно прочитано {len(transactions)} транзакций из Excel")
        return transactions

    except Exception as e:
        error_msg = f"Ошибка чтения Excel файла {file_path}: {str(e)}"
        logger.error(error_msg)
        raise  # Просто перебрасываем оригинальное исключение


def read_transactions(file_path: str) -> list[dict]:
    """
    Читает транзакции из файла (JSON/CSV/XLSX).

    Args:
        file_path: Путь к файлу с транзакциями

    Returns:
        Список словарей с транзакциями
    """
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == ".json":
        # Здесь будет чтение JSON
        return []
    elif file_ext == ".csv":
        return read_csv_file(file_path)
    elif file_ext in [".xlsx", ".xls"]:
        return read_excel_file(file_path)
    else:
        raise ValueError(f"Неподдерживаемый формат: {file_ext}")
