from pathlib import Path

print("ПРОВЕРКА СТРУКТУРЫ ПРОЕКТА")
print("=" * 30)

print("Текущая папка:", Path('.').absolute())

checks = [
    ("data/", Path("data").exists()),
    ("data/transactions_excel.xlsx", Path("data/transactions_excel.xlsx").exists()),
    ("main.py", Path("main.py").exists()),
    ("src/", Path("src").exists())
]

for name, exists in checks:
    status = "OK" if exists else "ERROR"
    print(f"{status} {name}")

if Path("data").exists():
    print("Файлы в data/:", [f.name for f in Path("data").iterdir()])

print("\nЗАВИСИМОСТИ:")
try:
    import pandas
    print("OK pandas")
except ImportError:
    print("ERROR pandas")

try:
    import openpyxl
    print("OK openpyxl")
except ImportError:
    print("ERROR openpyxl")

print("=" * 30)
print("Проект готов к работе!")
print("Запустите: python main.py")
