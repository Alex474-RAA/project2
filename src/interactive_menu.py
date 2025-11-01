import json

import pandas as pd

from src.external_api import convert_currency_to_rub
from src.processing import filter_by_state, sort_by_date
from src.search_operations import process_bank_operations, process_bank_search
from src.widget import get_date as format_date
from src.widget import mask_account_card


def read_json_file(file_path: str):
    """Чтение JSON файла напрямую"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_csv_file(file_path: str):
    """Чтение CSV файла"""
    df = pd.read_csv(file_path)
    return df.to_dict("records")


def read_excel_file(file_path: str):
    """Чтение Excel файла"""
    df = pd.read_excel(file_path)
    return df.to_dict("records")


def run_interactive_menu():
    """Запускает интерактивное меню согласно заданию"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("4. Вернуться к основному меню")

        choice = input("Ваш выбор: ").strip()

        if choice == "4":
            print("Возврат к основному меню...")
            break

        file_path = None
        if choice == "1":
            file_path = "data/operations.json"
            print("Для обработки выбран JSON-файл.")
        elif choice == "2":
            file_path = "data/transactions.csv"
            print("Для обработки выбран CSV-файл.")
        elif choice == "3":
            file_path = "data/transactions_excel.xlsx"
            print("Для обработки выбран XLSX-файл.")
        else:
            print("Неверный выбор. Попробуйте снова.")
            continue

        # Чтение транзакций - ПРОСТАЯ ВЕРСИЯ
        try:
            if choice == "1":
                transactions = read_json_file(file_path)
            elif choice == "2":
                transactions = read_csv_file(file_path)
            elif choice == "3":
                transactions = read_excel_file(file_path)

            if not transactions:
                print("Файл пуст или не содержит транзакций.")
                continue
            print(f"Прочитано {len(transactions)} транзакций.")
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
            continue

        # Фильтрация по статусу
        while True:
            print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")
            status = input("Статус: ").strip().upper()

            if status in ["EXECUTED", "CANCELED", "PENDING"]:
                filtered_transactions = filter_by_state(transactions, status)
                print(f'Операции отфильтрованы по статусу "{status}"')
                break
            else:
                print(f'Статус операции "{status}" недоступен.')

        if not filtered_transactions:
            print("Не найдено операций с выбранным статусом.")
            continue

        # Дополнительные фильтры
        filtered_data = filtered_transactions.copy()

        # Сортировка по дате
        sort_date = input("\nОтсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_date in ["да", "д", "yes", "y"]:
            sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            reverse = sort_order in ["по убыванию", "убыванию", "убывание", "desc"]
            filtered_data = sort_by_date(filtered_data, reverse=reverse)
            order_text = "по убыванию" if reverse else "по возрастанию"
            print(f"Операции отсортированы {order_text}")

        # Фильтрация по рублевым транзакциям
        rub_only = input("\nВыводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if rub_only in ["да", "д", "yes", "y"]:
            filtered_data = [
                t for t in filtered_data if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
            ]
            print("Оставлены только рублевые транзакции.")

        # Поиск по описанию
        search_desc = (
            input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
        )
        if search_desc in ["да", "д", "yes", "y"]:
            search_word = input("Введите слово для поиска в описании: ").strip()
            if search_word:
                filtered_data = process_bank_search(filtered_data, search_word)
                print(f'Найдено {len(filtered_data)} операций с словом "{search_word}" в описании')

        # Вывод результатов
        print("\n" + "=" * 50)
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_data)}")

        if not filtered_data:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            continue

        for transaction in filtered_data:
            print("\n" + "-" * 40)
            # Форматирование даты
            date_str = format_date(transaction.get("date", ""))
            print(date_str)

            # Описание
            description = transaction.get("description", "Нет описания")
            print(description)

            # Откуда и куда
            from_account = transaction.get("from", "")
            to_account = transaction.get("to", "")

            if from_account:
                masked_from = mask_account_card(from_account)
                print(f"{masked_from} -> ", end="")
            masked_to = mask_account_card(to_account)
            print(masked_to)

            # Сумма
            amount_info = transaction.get("operationAmount", {})
            amount = amount_info.get("amount", "0")
            currency = amount_info.get("currency", {})
            currency_name = currency.get("name", "")
            currency_code = currency.get("code", "")

            # Конвертация в рубли если нужно
            if currency_code != "RUB":
                try:
                    converted = convert_currency_to_rub(float(amount), currency_code)
                    print(f"Сумма: {amount} {currency_name} (~{converted:.2f} руб.)")
                except Exception:
                    print(f"Сумма: {amount} {currency_name}")
            else:
                print(f"Сумма: {amount} {currency_name}")

        # Подсчет категорий
        print("\n" + "=" * 50)
        categories = ["Перевод", "Вклад", "Оплата", "Карта", "Счет"]
        category_counts = process_bank_operations(filtered_data, categories)
        print("Статистика по категориям:")
        for category, count in category_counts.items():
            if count > 0:
                print(f"  {category}: {count} операций")
