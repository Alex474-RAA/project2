import json
from datetime import datetime
from typing import Dict, List


def get_date(date_iso: str) -> str:
    """
    Принимает на вход строку с датой в формате ISO.
    Возвращает строку с датой в формате "ДД.ММ.ГГГГ".

    :param date_iso: Строка с датой в формате ISO.
    :return: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    date = datetime.fromisoformat(date_iso)
    return date.strftime("%d.%m.%Y")


def load_json_data(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список в случае ошибки.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Проверяем, что данные являются списком
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
