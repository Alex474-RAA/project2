from pathlib import Path

print("СТРУКТУРА ПРОЕКТА:")
print("=" * 30)

# Проверим что есть в src
src_path = Path("src")
if src_path.exists():
    print("Файлы в src/:")
    for file in src_path.iterdir():
        if file.is_file():
            print(f"  - {file.name}")

# Проверим data
data_path = Path("data")
if data_path.exists():
    print("\nФайлы в data/:")
    for file in data_path.iterdir():
        print(f"  - {file.name}")

print("\n" + "=" * 30)
