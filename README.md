# Обработка банковских транзакций

    Небольшая утилита для работы с банковскими транзакциями на Python. Позволяет:
    1. Маскировать номера карт и счетов
    2. Фильтровать транзакции по валюте
    3. Сортировать транзакции по дате
    4. Генерировать тестовые номера карт
## Основные функции

### Маскирование номера карты

    `masked_card = mask_account_card("Visa Platinum 8990922113665229")
    print(masked_card)  # Visa Platinum 8990 92** **** 5229`
### Маскирование номера счёта

    `masked_account = mask_account_card("Счет 73654108430135874305")
    print(masked_account)  # Счет **4305`

### Фильтрация транзакций

    `transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}}
    ]`
### Фильтрация по валюте

    `usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
    print(transaction)`

### Сортировка по дате

    1. Сортировка от новых к старым
    `sorted_transactions = sort_by_date(transactions)`
    2. Сортировка от старых к новым
    `sorted_asc = sort_by_date(transactions, reverse=False)`

### Генерация номеров карт

    1. Генерация тестовых номеров карт
    `for card_number in card_number_generator(1, 3):
    print(card_number)
    Вывод:
    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003`

## Запуск тестов

    Для проверки работы модулей используются pytest и unittest:
    `pytest tests/
     python -m unittest tests/test_processing.py`

## Функции тестов

### Обработка ошибок

    Система валидации проверяет:
    Длину номеров (карты: 16 цифр, счета: ≥4 цифр)
    Цифровой формат номеров
    Корректность дат (ISO-формат)
    Наличие обязательных полей в транзакциях
    При ошибках вызываются исключения ValueError или TypeError.

### Маскировка номеров карт и счетов

    `get_mask_card_number(card_number: str) -> str`:
     Принимает номер карты (16 цифр, возможно с пробелами) и возвращает его в формате "XXXX XX** **** XXXX".
     Если номер не содержит 16 цифр или содержит нецифровые символы, вызывает `ValueError`.

    `get_mask_account(account_number: str) -> str`:
     Принимает номер счета (не менее 4 цифр) и возвращает строку в формате "**XXXX", где XXXX - последние 4 цифры счета.
     Если номер счета содержит меньше 4 цифр или не только цифры, вызывает `ValueError`.

    `mask_account_card(data: str) -> str`:
     Принимает строку, содержащую тип карты/счета и номер (например, "Visa Platinum 8990922113665229" или "Счет 73654108430135874303").
     Возвращает строку с маскированным номером в соответствующем формате.
     Для карт: оставляет первые 6 цифр (разбивая на группы по 4) и маскирует следующие 6, оставляя последние 4.
     Для счетов: оставляет только последние 4 цифры с префиксом "**".
     Если данные не соответствуют ожидаемому формату, вызывает `ValueError`.

### Фильтрация и сортировка транзакций

    `filter_by_state(transactions: list[dict], state: str) -> list[dict]`:
     Фильтрует список транзакций по статусу `state` (например, "EXECUTED").
     Возвращает новый список. Транзакции без ключа 'state' пропускаются.

    `sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]`:
     Сортирует транзакции по дате (ключ 'date') в порядке убывания (по умолчанию). Если `reverse=False` - по возрастанию.
     Транзакции без даты или с некорректной датой помещаются в конец.

### Работа с датами

    `get_date(iso_date: str) -> str`:
     Преобразует дату в формате ISO (например, "2023-06-20T00:00:00.000000") в строку формата "ДД.ММ.ГГГГ".
     Если формат неверный, вызывает `ValueError`.

### Генераторы

    `card_number_generator(start: int, end: int) -> Generator[str, None, None]`:
     Генерирует номера карт в диапазоне от `start` до `end` (включительно) в формате "XXXX XXXX XXXX XXXX".

    `filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]`
     Фильтрует транзакции по коду валюты (например, "USD") и возвращает генератор.

    `transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]`:
     Возвращает генератор описаний транзакций (ключ 'description').

## Требования
    - Python 3.9+
    - Зависимости: pytest (для тестирования)

## Автор
      Ревякин А.и И.И 