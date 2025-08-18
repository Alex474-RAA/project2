def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """Генератор для фильтрации транзакций по валюте"""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> iter:
    """Генератор для извлечения описаний транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> iter:
    """Генератор номеров банковских карт в заданном диапазоне"""
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
