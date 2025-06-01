from src.masks import get_mask_card_number, get_mask_account


if __name__ == "__main__":
    # Пример использования маскировки номера карты
    print(get_mask_card_number("7000792289606361"))  # Вывод: 7000 79** **** 6361

    # Пример использования маскировки счёта
    print(get_mask_account("73654108430135874305"))  # Вывод: **4305

