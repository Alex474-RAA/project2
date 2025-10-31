import re
from collections import Counter
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет операции по строке в описании с использованием регулярных выражений.

    Args:
        data: Список словарей с транзакциями
        search: Строка для поиска в описании

    Returns:
        Список словарей с найденными операциями
    """
    try:
        pattern = re.compile(search, re.IGNORECASE)
        return [op for op in data if pattern.search(op.get('description', ''))]
    except re.error:
        # Если некорректное регулярное выражение, ищем как обычную строку
        return [op for op in data if search.lower() in op.get('description', '').lower()]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    Args:
        data: Список словарей с транзакциями
        categories: Список категорий для подсчета

    Returns:
        Словарь с количеством операций по категориям
    """
    # Используем Counter как требуется в задании
    all_descriptions = []
    for op in data:
        description = op.get('description', '').lower()
        all_descriptions.append(description)

    # Создаем счетчик для всех описаний
    description_counter = Counter(all_descriptions)

    # Фильтруем только нужные категории
    category_counts = {}
    for category in categories:
        category_lower = category.lower()
        count = sum(
            count for desc, count in description_counter.items()
            if category_lower in desc
        )
        category_counts[category] = count

    return category_counts
