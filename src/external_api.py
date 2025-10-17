import os
from typing import Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()


def convert_currency_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях (float).
    """
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    # Если валюта уже рубли, возвращаем как есть
    if currency == 'RUB':
        return amount

    # Получаем курс валюты к рублю
    exchange_rate = get_exchange_rate(currency)

    # Конвертируем сумму
    return amount * exchange_rate


def get_exchange_rate(currency: str) -> float:
    """
    Получает текущий курс валюты к рублю через внешнее API.

    :param currency: Код валюты (USD, EUR и т.д.)
    :return: Курс валюты к рублю.
    """
    api_key = os.getenv('EXCHANGE_RATE_API_KEY')

    if not api_key:
        raise ValueError("API ключ для конвертации валют не найден")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Ошибка при получении курса валют: {response.status_code}")

    data = response.json()

    if 'rates' not in data or 'RUB' not in data['rates']:
        raise Exception("Не удалось получить курс рубля")

    rub_rate = data['rates']['RUB']
    return float(rub_rate)  # Явное преобразование к float
