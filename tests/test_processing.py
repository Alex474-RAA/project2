import unittest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date

class TestProcessingFunctions(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных."""
        self.test_transactions = [
            {"id": 1, "state": "EXECUTED", "date": "2023-06-20"},
            {"id": 2, "state": "PENDING", "date": "2023-07-15"},
            {"id": 3, "state": "EXECUTED", "date": "2023-01-10"},
            {"id": 4, "date": "2022-12-25"},  # Нет ключа 'state'
            {"id": 5, "state": "CANCELED", "date": "2023-03-05"},
            {"id": 6, "state": "EXECUTED", "date": "invalid-date"},  # Некорректная дата
        ]

    # Тесты для filter_by_state
    def test_filter_by_state_executed(self):
        result = filter_by_state(self.test_transactions, "EXECUTED")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 3)
        self.assertEqual(result[2]["id"], 6)

    def test_filter_by_state_pending(self):
        result = filter_by_state(self.test_transactions, "PENDING")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 2)

    def test_filter_by_state_empty_list(self):
        result = filter_by_state([], "EXECUTED")
        self.assertEqual(result, [])

    def test_filter_by_state_missing_state(self):
        with self.assertRaises(ValueError):
            filter_by_state(self.test_transactions, None)

    def test_filter_by_state_invalid_input(self):
        with self.assertRaises(TypeError):
            filter_by_state("not a list", "EXECUTED")
        with self.assertRaises(TypeError):
            filter_by_state([{"state": "EXECUTED"}, "not a dict"], "EXECUTED")

    # Тесты для sort_by_date
    def test_sort_by_date_descending(self):
        result = sort_by_date(self.test_transactions)
        ids = [t["id"] for t in result]
        self.assertEqual(ids, [2, 1, 5, 3, 4, 6])

    def test_sort_by_date_ascending(self):
        result = sort_by_date(self.test_transactions, reverse=False)
        ids = [t["id"] for t in result]
        self.assertEqual(ids, [6, 4, 3, 5, 1, 2])

    def test_sort_by_date_missing_date(self):
        test_data = [{"id": 1}, {"id": 2, "date": "2023-01-01"}]
        result = sort_by_date(test_data)
        self.assertEqual([t["id"] for t in result], [2, 1])

    def test_sort_by_date_invalid_format(self):
        test_data = [
            {"id": 1, "date": "2023-01-01"},
            {"id": 2, "date": "invalid-date"},
            {"id": 3}  # Полностью отсутствует дата
        ]
        result = sort_by_date(test_data)
        self.assertEqual([t["id"] for t in result], [1, 2, 3])

    def test_sort_by_date_empty_list(self):
        result = sort_by_date([])
        self.assertEqual(result, [])

    def test_sort_by_date_single_element(self):
        test_data = [{"date": "2023-01-01"}]
        result = sort_by_date(test_data)
        self.assertEqual(result, test_data)

    def test_sort_by_date_identical_dates(self):
        test_data = [
            {"id": 1, "date": "2023-01-01"},
            {"id": 2, "date": "2023-01-01"}
        ]
        result = sort_by_date(test_data)
        self.assertEqual(len(result), 2)
        self.assertEqual([t["id"] for t in result], [1, 2])

    # Тесты для покрытия обработки исключений
    def test_sort_by_date_invalid_date_format(self):
        """Тест невалидного строкового формата даты"""
        test_data = [
            {"id": 1, "date": "2023-01-01"},
            {"id": 2, "date": "неправильный-формат-даты"}
        ]
        result = sort_by_date(test_data)
        # Проверяем что валидная дата идет первой
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 2)

    def test_sort_by_date_invalid_date_type(self):
        """Тест неверного типа данных в поле даты"""
        test_data = [
            {"id": 1, "date": 20230101},  # Число вместо строки
            {"id": 2, "date": {"day": 1, "month": 1, "year": 2023}},  # Словарь
            {"id": 3, "date": ["2023", "01", "01"]},  # Список
            {"id": 4, "date": "2023-01-01"}  # Валидная дата
        ]
        result = sort_by_date(test_data)
        # Валидная дата должна быть первой
        self.assertEqual(result[0]["id"], 4)
        # Остальные в исходном порядке
        self.assertEqual(result[1]["id"], 1)
        self.assertEqual(result[2]["id"], 2)
        self.assertEqual(result[3]["id"], 3)

    def test_sort_by_date_none_value(self):
        """Тест None значения в поле даты"""
        test_data = [
            {"id": 1, "date": None},
            {"id": 2, "date": "2023-01-01"}
        ]
        result = sort_by_date(test_data)
        self.assertEqual(result[0]["id"], 2)
        self.assertEqual(result[1]["id"], 1)

    def test_sort_by_date_mixed_invalid(self):
        """Тест смешанных валидных и невалидных дат"""
        test_data = [
            {"id": 1, "date": "invalid"},
            {"id": 2, "date": "2024-01-01"},
            {"id": 3, "date": "2023-01-01"},
            {"id": 4},  # Нет даты
            {"id": 5, "date": 12345}
        ]
        result = sort_by_date(test_data)
        # Валидные даты в порядке убывания
        self.assertEqual(result[0]["id"], 2)  # 2024-01-01
        self.assertEqual(result[1]["id"], 3)  # 2023-01-01
        # Невалидные даты в исходном порядке
        self.assertEqual(result[2]["id"], 1)
        self.assertEqual(result[3]["id"], 4)
        self.assertEqual(result[4]["id"], 5)

if __name__ == "__main__":
    unittest.main()