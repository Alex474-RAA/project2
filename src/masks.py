def get_mask_card_number(card_number: str) -> str:
    # Удаляем все пробелы (если они есть) и проверяем, что номер состоит из цифр
    cleaned_number = card_number.replace(" ", "")
    if not cleaned_number.isdigit() or len(cleaned_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")

    # Разбиваем на части: первые 6 и последние 4 цифры
    first_part = cleaned_number[:6]
    last_part = cleaned_number[-4:]

    # Маскируем среднюю часть (6*)
    masked_part = "**** **"

    # Формируем итоговую строку
    masked_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"

    return masked_number






def get_mask_account(account_number: str) -> str:
    # Удаляем пробелы (если есть) и проверяем, что номер состоит из цифр
    cleaned_number = account_number.replace(" ", "")
    if not cleaned_number.isdigit() or len(cleaned_number) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    # Берём последние 4 цифры и добавляем ** в начало
    masked_account = f"**{cleaned_number[-4:]}"

    return masked_account



