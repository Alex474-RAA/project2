from pathlib import Path  # современная замена os.path

import pandas as pd


def read_transactions_file(file_path="data/transactions_excel.xlsx"):
    try:
        # Используем pathlib вместо os
        path = Path(file_path)

        if not path.exists():
            print(f"❌ Ошибка: Файл {file_path} не найден")
            print("Проверьте:")
            print("1. Что файл существует")
            print("2. Что путь указан правильно")
            print("3. Что файл называется 'transactions_excel.xlsx'")
            return None

        # Читаем Excel файл
        df = pd.read_excel(path)

        print("✅ Файл успешно прочитан!")
        print(f"📊 Размер данных: {df.shape[0]} строк, {df.shape[1]} колонок")
        print(f"📋 Колонки: {', '.join(df.columns)}")

        return df

    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return None


# Использование
if __name__ == "__main__":
    data = read_transactions_file()

    if data is not None:
        print("\n🔍 Первые 3 строки данных:")
        print(data.head(3))
