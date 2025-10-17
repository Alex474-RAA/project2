import logging
import os

# Создаем папку logs если её нет
os.makedirs('logs', exist_ok=True)

# Настройка логера для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# File handler для masks
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Formatter с меткой времени, именем модуля, уровнем и сообщением
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    try:
        # Удаляем все пробелы (если они есть) и проверяем, что номер состоит из цифр
        cleaned_number = card_number.replace(" ", "")
        if not cleaned_number.isdigit() or len(cleaned_number) != 16:
            logger.error("Номер карты должен состоять из 16 цифр")
            raise ValueError("Номер карты должен состоять из 16 цифр")

        # Разбиваем на части: первые 6 и последние 4 цифры
        first_part = cleaned_number[:6]
        last_part = cleaned_number[-4:]

        # Маскируем среднюю часть (6*)
        masked_part = "** ****"

        # Формируем итоговую строку
        masked_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"

        logger.info("Успешное маскирование номера карты")
        return masked_number

    except Exception as e:
        logger.error(f"Ошибка при маскировании карты: {type(e).__name__}")
        raise


def get_mask_account(account_number: str) -> str:
    try:
        # Удаляем пробелы (если есть) и проверяем, что номер состоит из цифр
        cleaned_number = account_number.replace(" ", "")
        if not cleaned_number.isdigit() or len(cleaned_number) < 4:
            logger.error("Номер счёта должен содержать минимум 4 цифры")
            raise ValueError("Номер счёта должен содержать минимум 4 цифры")

        # Берём последние 4 цифры и добавляем ** в начало
        masked_account = f"**{cleaned_number[-4:]}"

        logger.info("Успешное маскирование номера счета")
        return masked_account

    except Exception as e:
        logger.error(f"Ошибка при маскировании счета: {type(e).__name__}")
        raise
