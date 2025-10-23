import pandas as pd
import os


def create_excel_file():
    """Создает тестовый Excel файл с транзакциями"""

    # Создаем папку data если её нет
    os.makedirs('data', exist_ok=True)

    # Создаем тестовые данные
    data = {
        'id': [1, 2, 3, 4, 5],
        'date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
        'amount': [100.50, 200.00, 1500.00, 50.75, 300.00],
        'currency': ['USD', 'EUR', 'RUB', 'USD', 'EUR'],
        'description': [
            'Покупка в магазине',
            'Онлайн подписка',
            'Перевод другу',
            'Возврат средств',
            'Оплата услуг'
        ],
        'from_account': [
            'Maestro 1596837868705199',
            'Visa Classic 6831982476737658',
            'MasterCard 7158300734726758',
            'Счет 48894435694657040768',
            'Visa Gold 5999414228426353'
        ],
        'to_account': [
            'Счет 64686473678894779589',
            'Счет 64686473678894779589',
            'Счет 35383033474447895560',
            'Visa Platinum 8990922113665229',
            'Счет 38976430693692818358'
        ],
        'status': ['EXECUTED', 'EXECUTED', 'PENDING', 'EXECUTED', 'CANCELED']
    }

    # Создаем DataFrame
    df = pd.DataFrame(data)

    # Сохраняем в Excel
    df.to_excel('data/transactions_excel.xlsx', index=False, sheet_name='Transactions')

    print("✅ Excel файл создан: data/transactions_excel.xlsx")
    print(f"✅ Создано {len(df)} транзакций")

    # Показываем содержимое
    print("\nСодержимое файла:")
    print(df.head())


if __name__ == "__main__":
    create_excel_file()
    