import os
from dotenv import load_dotenv
import requests

# Загружаем переменные окружения
load_dotenv()

api_key = os.getenv('EXCHANGE_RATE_API_KEY')

if not api_key:
    print("API ключ не найден в .env файле.")
    exit(1)

url = "https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB"

headers = {
    "apikey": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Успешный запрос!")
    print(f"Курс USD к RUB: {data['rates']['RUB']}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
