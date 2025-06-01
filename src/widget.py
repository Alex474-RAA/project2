from datetime import datetime
from .masks import mask_card, mask_account


def mask_account_card(input_str: str) -> str:
    """
    Маскирует номер карты/счета в строке формата:
    'Visa Platinum 7000792289606361' → 'Visa Platinum 7000 79** **** 6361'
    'Счет 73654108430135874305' → 'Счет **4305'
    """
    parts = input_str.split()
    number = parts[-1]

    if "счет" in input_str.lower():
        return ' '.join(parts[:-1] + [mask_account(number)])
    else:
        return ' '.join(parts[:-1] + [mask_card(number)])


def get_date(date_str: str) -> str:
    """
    Преобразует дату из строки в формат 'DD.MM.YYYY'.
    Пример: '2018-07-11' → '11.07.2018'
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты. Ожидается 'YYYY-MM-DD'")