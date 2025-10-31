import pytest

from src.search_operations import process_bank_operations, process_bank_search


class TestSearchOperations:
    """Тесты для функций поиска и подсчета операций"""

    @pytest.fixture
    def sample_transactions(self):
        return [
            {"id": 1, "description": "Перевод организации", "state": "EXECUTED", "date": "2023-01-01"},
            {"id": 2, "description": "Открытие вклада", "state": "EXECUTED", "date": "2023-01-02"},
            {"id": 3, "description": "Перевод с карты на карту", "state": "CANCELED", "date": "2023-01-03"},
            {"id": 4, "description": "Оплата услуг", "state": "EXECUTED", "date": "2023-01-04"},
        ]

    def test_process_bank_search_found(self, sample_transactions):
        """Тест поиска операций по строке"""
        result = process_bank_search(sample_transactions, "Перевод")
        assert len(result) == 2
        assert all("Перевод" in op["description"] for op in result)

    def test_process_bank_search_not_found(self, sample_transactions):
        """Тест поиска когда ничего не найдено"""
        result = process_bank_search(sample_transactions, "Несуществующий")
        assert len(result) == 0

    def test_process_bank_search_case_insensitive(self, sample_transactions):
        """Тест поиска без учета регистра"""
        result = process_bank_search(sample_transactions, "перевод")
        assert len(result) == 2

    def test_process_bank_operations_single_category(self, sample_transactions):
        """Тест подсчета операций для одной категории"""
        result = process_bank_operations(sample_transactions, ["Перевод"])
        assert result == {"Перевод": 2}

    def test_process_bank_operations_multiple_categories(self, sample_transactions):
        """Тест подсчета операций для нескольких категорий"""
        result = process_bank_operations(
            sample_transactions, ["Перевод", "Вклад", "Оплата"]  # Изменили "Услуги" на "Оплата"
        )
        expected = {"Перевод": 2, "Вклад": 1, "Оплата": 1}
        assert result == expected

    def test_process_bank_operations_no_matches(self, sample_transactions):
        """Тест подсчета когда категории не найдены"""
        result = process_bank_operations(sample_transactions, ["Кредит"])
        assert result == {"Кредит": 0}

    def test_process_bank_operations_empty_data(self):
        """Тест подсчета с пустыми данными"""
        result = process_bank_operations([], ["Перевод"])
        assert result == {"Перевод": 0}
