from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список транзакций по значению ключа 'state'.

    Параметры:
        transactions: Список словарей с транзакциями
        state: Значение для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
        Отфильтрованный список транзакций, где state совпадает с заданным

    Пример:
        >>> filter_by_state([{'state': 'EXECUTED'}], 'EXECUTED')
        [{'state': 'EXECUTED'}]
    """
    return [t for t in transactions if t.get('state') == state]


from typing import List, Dict
from datetime import datetime


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

    def get_date(item):
        date_str = item.get('date', '')
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except (ValueError, TypeError):
            return datetime.min  # Для некорректных/отсутствующих дат

    return sorted(
        transactions,
        key=get_date,
        reverse=reverse
    )

