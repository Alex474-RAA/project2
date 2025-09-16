import pytest
import os
from unittest.mock import patch, MagicMock
from src.external_api import convert_currency_to_rub, get_exchange_rate


def test_convert_currency_to_rub_rub():
    """Тест конвертации рублей в рубли (должен вернуть ту же сумму)."""
    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {
                'code': 'RUB'
            }
        }
    }

    result = convert_currency_to_rub(transaction)
    assert result == 100.0


@patch('src.external_api.get_exchange_rate')
def test_convert_currency_to_rub_usd(mock_get_rate):
    """Тест конвертации USD в рубли."""
    mock_get_rate.return_value = 75.0

    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {
                'code': 'USD'
            }
        }
    }

    result = convert_currency_to_rub(transaction)
    assert result == 7500.0  # 100 * 75


@patch('src.external_api.requests.get')
def test_get_exchange_rate_success(mock_get):
    """Тест успешного получения курса валют."""
    # Мокируем ответ API
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'rates': {
            'RUB': 75.0
        }
    }
    mock_get.return_value = mock_response

    # Мокируем переменную окружения
    with patch.dict('os.environ', {'EXCHANGE_RATE_API_KEY': 'test_key'}):
        rate = get_exchange_rate('USD')
        assert rate == 75.0


@patch('src.external_api.requests.get')
def test_get_exchange_rate_failure(mock_get):
    """Тест обработки ошибки при получении курса валют."""
    # Мокируем ответ API с ошибкой
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    # Мокируем переменную окружения
    with patch.dict('os.environ', {'EXCHANGE_RATE_API_KEY': 'test_key'}):
        with pytest.raises(Exception, match="Ошибка при получении курса валют: 500"):
            get_exchange_rate('USD')


def test_get_exchange_rate_no_api_key():
    """Тест обработки отсутствия API ключа."""
    # Убедимся, что переменная окружения не установлена
    if 'EXCHANGE_RATE_API_KEY' in os.environ:
        del os.environ['EXCHANGE_RATE_API_KEY']

    with pytest.raises(ValueError, match="API ключ для конвертации валют не найден"):
        get_exchange_rate('USD')