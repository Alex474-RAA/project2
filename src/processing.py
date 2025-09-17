from datetime import datetime
from typing import Dict, List, Callable


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список транзакций по значению ключа 'state'.

    Параметры:
        transactions: Список словарей с транзакциями
        state: Значение для фильтрации (по умолчанию "EXECUTED")

    Возвращает:
        Отфильтрованный список транзакций, где state совпадает с заданным

    Исключения:
        TypeError: Если transactions не список или элементы не словари
        ValueError: Если state не указан

    Пример:
        >>> filter_by_state([{'state': 'EXECUTED'}], 'EXECUTED')
        [{'state': 'EXECUTED'}]
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions должен быть списком")

    if state is None:
        raise ValueError("state обязателен для указания")

    result_list = []
    for item in transactions:
        if not isinstance(item, dict):
            raise TypeError("элемент transactions должен быть словарём")
        if item.get("state") == state:
            result_list.append(item)

    return result_list


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список транзакций по дате (ключ 'date').

    Параметры:
        transactions: Список словарей с транзакциями
        reverse: Если True (по умолчанию) - сортировка по убыванию (новые сначала),
                 Если False - по возрастанию (старые сначала)

    Возвращает:
        Новый отсортированный список транзакций

    Пример:
        >>> sort_by_date([{'date': '2023-01-01'}, {'date': '2024-01-01'}])
        [{'date': '2024-01-01'}, {'date': '2023-01-01'}]
    """

    def get_date(item: Dict) -> datetime:
        date_str = item.get("date", "")
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except (ValueError, TypeError):
            return datetime.min  # Для некорректных/отсутствующих дат

    return sorted(transactions, key=get_date, reverse=reverse)
