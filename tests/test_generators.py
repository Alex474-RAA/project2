import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фикстура с тестовыми данными
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
        }
    ]

# Тесты для filter_by_currency
def test_filter_by_currency(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    with pytest.raises(StopIteration):
        next(usd_transactions)

def test_filter_empty_list():
    assert list(filter_by_currency([], "USD")) == []

def test_filter_no_match(sample_transactions):
    assert list(filter_by_currency(sample_transactions, "EUR")) == []

# Тесты для transaction_descriptions
def test_transaction_descriptions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        next(descriptions)

def test_descriptions_empty_list():
    assert list(transaction_descriptions([])) == []

# Тесты для card_number_generator
@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected

def test_card_number_format():
    card_gen = card_number_generator(1234567890123456, 1234567890123456)
    assert next(card_gen) == "1234 5678 9012 3456"
