from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.interactive_menu import run_interactive_menu


def main():
    """Основная функция программы с двумя режимами работы"""
    while True:
        print("\n" + "=" * 50)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 50)
        print("1. Демонстрация функций (старый режим)")
        print("2. Интерактивная работа с транзакциями (новый режим)")
        print("3. Выйти")

        choice = input("Выберите режим работы: ").strip()

        if choice == "1":
            # Старая логика
            demo_old_functions()
        elif choice == "2":
            # Новая логика
            run_interactive_menu()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def demo_old_functions():
    """Демонстрация старых функций """
    # Пример использования маскировки номера карты
    print(get_mask_card_number("7000792289606361"))  # Вывод: 7000 79** **** 6361

    # Пример использования маскировки счёта
    print(get_mask_account("73654108430135874305"))  # Вывод: **4305

    # Пример данных
    transactions = [
        {"id": 1, "state": "EXECUTED", "amount": "100 USD"},
        {"id": 2, "state": "PENDING", "amount": "200 USD"},
        {"id": 3, "state": "EXECUTED", "amount": "300 USD"},
        {"id": 4, "state": "CANCELED", "amount": "400 USD"},
    ]

    # Фильтрация по умолчанию (EXECUTED)
    executed = filter_by_state(transactions)
    print("EXECUTED:", executed)

    # Фильтрация по другому состоянию
    pending = filter_by_state(transactions, "PENDING")
    print("PENDING:", pending)

    # Тестовые данные
    transactions = [
        {"id": 1, "date": "2023-06-20", "state": "EXECUTED"},
        {"id": 2, "date": "2023-07-15", "state": "PENDING"},
        {"id": 3, "date": "2023-01-10", "state": "EXECUTED"},
        {"id": 4, "date": "2022-12-25", "state": "CANCELED"},
    ]

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


if __name__ == "__main__":
    main()
