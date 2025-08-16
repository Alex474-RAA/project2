# Обработка банковских транзакций

    Программа для работы с банковскими транзакциями. Основные функции:
    1. Маскирование номеров карт и счетов
    2. Фильтрация транзакций по валюте
    3. Сортировка транзакций по дате
    4. Генерация тестовых номеров карт

## Как использовать

### Маскирование данных

from src.masks import mask_account_card

# Маскирование карты
print(mask_account_card("Visa Platinum 8990922113665229"))  # Visa Platinum 8990 92** **** 5229

# Маскирование счёта
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305
Фильтрация транзакций
python
from src.generators import filter_by_currency

transactions = [{"operationAmount": {"currency": {"code": "USD"}}}]
for transaction in filter_by_currency(transactions, "USD"):
    print(transaction)
Сортировка по дате
python
from src.processing import sort_by_date

transactions = [{"date": "2023-06-20"}, {"date": "2023-01-10"}]
sorted_trans = sort_by_date(transactions)  # Новые сначала
Генерация номеров карт
python
from src.generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)  # 0000 0000 0000 0001, 0000 0000 0000 0002 и т.д.
Запуск тестов
text
pytest tests/
python -m unittest tests/test_processing.py
Структура проекта
text
src/
├── masks.py          # Маскирование данных
├── utils.py          # Работа с датами
├── generators.py     # Генераторы данных
└── processing.py     # Обработка транзакций

tests/               # Тесты
Автор: [Ваше Имя]
