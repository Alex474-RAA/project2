from src.masks import get_mask_card_number, get_mask_account

# Маска
if __name__ == "__main__":
    # Пример использования маскировки номера карты
    print(get_mask_card_number("7000792289606361"))  # Вывод: 7000 79** **** 6361

    # Пример использования маскировки счёта
    print(get_mask_account("73654108430135874305"))  # Вывод: **4305


# !!!! ВЫДАЁТ ОШИБКУ !!!
# Маска карты
#from src.utils import mask_account_card, get_date

#print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
#print(mask_account_card("Счет 73654108430135874305"))       # Счет **4305
#print(get_date("2018-07-11"))                              # 11.07.2018



# Фильтр
from src.processing import filter_by_state

# Пример данных
transactions = [
    {'id': 1, 'state': 'EXECUTED', 'amount': '100 USD'},
    {'id': 2, 'state': 'PENDING', 'amount': '200 USD'},
    {'id': 3, 'state': 'EXECUTED', 'amount': '300 USD'},
    {'id': 4, 'state': 'CANCELED', 'amount': '400 USD'}
]

# Фильтрация по умолчанию (EXECUTED)
executed = filter_by_state(transactions)
print("EXECUTED:", executed)

# Фильтрация по другому состоянию
pending = filter_by_state(transactions, 'PENDING')
print("PENDING:", pending)


# Фильтация по убыванию и возростанию
from src.processing import filter_by_state, sort_by_date

# Тестовые данные
transactions = [
    {"id": 1, "date": "2023-06-20", "state": "EXECUTED"},
    {"id": 2, "date": "2023-07-15", "state": "PENDING"},
    {"id": 3, "date": "2023-01-10", "state": "EXECUTED"},
    {"id": 4, "date": "2022-12-25", "state": "CANCELED"}
]

if __name__ == "__main__":
    # Фильтрация
    executed = filter_by_state(transactions)
    print("EXECUTED транзакции:", executed)

    # Сортировка
    newest_first = sort_by_date(executed)
    print("\nНовые EXECUTED транзакции сначала:")
    for t in newest_first:
        print(f"{t['date']} (ID: {t['id']})")

    oldest_first = sort_by_date(executed, reverse=False)
    print("\nСтарые EXECUTED транзакции сначала:")
    for t in oldest_first:
        print(f"{t['date']} (ID: {t['id']})")

