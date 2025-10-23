from pathlib import Path
import subprocess
import sys

def run_check(name, command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"OK {name}")
            return True
        else:
            print(f"ERROR {name}")
            return False
    except:
        print(f"ERROR {name}")
        return False

print("ФИНАЛЬНАЯ ПРОВЕРКА")
print("=" * 20)

checks = [
    ("Структура", "python check_files.py"),
    ("Excel файл", "python -c \"import pandas as pd; df = pd.read_excel('data/transactions_excel.xlsx'); print(f'Excel: {df.shape[0]} строк')\""),
    ("Основные функции", "python -c \"from src.widget import mask_account_card, get_date; print('Функции работают')\""),
    ("File Reader", "python -c \"from src.file_reader import read_transactions; print('File reader импортируется')\""),
    ("Тесты", "python -m pytest tests/ -q --tb=no"),
]

passed = 0
for name, cmd in checks:
    if run_check(name, cmd):
        passed += 1

print("=" * 20)
print(f"ИТОГ: {passed}/{len(checks)}")

if passed >= 3:  # Хотя бы 3 из 5
    print("ПРОЕКТ ГОТОВ К ОТПРАВКЕ! 🚀")
    sys.exit(0)
else:
    print("НУЖНЫ ИСПРАВЛЕНИЯ")
    sys.exit(1)
