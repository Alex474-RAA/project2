# Обработка банковских транзакций

    Небольшая утилита для работы с банковскими транзакциями на Python. Позволяет:
     1. Маскировать номера карт и счетов
     2. Фильтровать транзакции по валюте
     3. Сортировать транзакции по дате
     4. Генерировать тестовые номера карт

## Основные функции

### Маскирование данных

### Маскирование номера карты
    masked_card = mask_account_card("Visa Platinum 8990922113665229")
    print(masked_card)  # Visa Platinum 8990 92** **** 5229

### Маскирование номера счёта
    masked_account = mask_account_card("Счет 73654108430135874305")
    print(masked_account)  # Счет **4305
### Фильтрация транзакций

    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}}
    ]

### Фильтрация по валюте
    usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
    print(transaction)
### Сортировка по дате

### Сортировка от новых к старым
    sorted_transactions = sort_by_date(transactions)

### Сортировка от старых к новым
    sorted_asc = sort_by_date(transactions, reverse=False)
### Генерация номеров карт

### Генерация тестовых номеров карт
    for card_number in card_number_generator(1, 3):
    print(card_number)
    # Вывод:
    # 0000 0000 0000 0001
    # 0000 0000 0000 0002
    # 0000 0000 0000 0003

# Запуск тестов
    Для проверки работы модулей используются pytest и unittest:

    text
    pytest tests/
    python -m unittest tests/test_processing.py

# Требования
    Python 3.9+

# Зависимости: pytest (для тестирования)

# Автор: [Ревякин Александр],[И.И]

# Этот проект лицензирован по лицензии MIT.