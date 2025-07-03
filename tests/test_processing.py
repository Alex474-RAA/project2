import unittest

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
        ]

    # Тесты для filter_by_state
    def test_filter_by_state_executed(self):
        result = filter_by_state(self.test_transactions, "EXECUTED")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 3)

    def test_filter_by_state_pending(self):
        result = filter_by_state(self.test_transactions, "PENDING")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 2)

    #def test_filter_by_state_missing_state(self):
        #with self.assertRaises(ValueError):
            #filter_by_state(self.test_transactions[:3], "EXECUTED")

    def test_filter_by_state_invalid_input(self):
        with self.assertRaises(TypeError):
            filter_by_state("not a list", "EXECUTED")
        with self.assertRaises(TypeError):
            filter_by_state([{"state": "EXECUTED"}, "not a dict"], "EXECUTED")

    # Тесты для sort_by_date
    def test_sort_by_date_descending(self):
        result = sort_by_date(self.test_transactions)
        dates = [t["date"] for t in result if "date" in t]
        self.assertEqual(dates, ["2023-07-15", "2023-06-20", "2023-03-05", "2023-01-10", "2022-12-25"])

    def test_sort_by_date_ascending(self):
        result = sort_by_date(self.test_transactions, reverse=False)
        dates = [t["date"] for t in result if "date" in t]
        self.assertEqual(dates, ["2022-12-25", "2023-01-10", "2023-03-05", "2023-06-20", "2023-07-15"])

    def test_sort_by_date_missing_date(self):
        test_data = [{"id": 1}, {"id": 2, "date": "2023-01-01"}]
        result = sort_by_date(test_data)
        self.assertEqual(len(result), 2)  # Должен работать даже с отсутствующими датами

    def test_sort_by_date_invalid_format(self):
        test_data = [{"date": "2023-01-01"}, {"date": "invalid-date"}]
        result = sort_by_date(test_data)
        self.assertEqual(result[0]["date"], "2023-01-01")  # Некорректные даты должны попадать в конец


if __name__ == "__main__":
     run_tests()