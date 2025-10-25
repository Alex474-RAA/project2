import os
import sys
import unittest
from unittest.mock import patch

import pandas as pd

from src.file_reader import read_csv_file, read_excel_file

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestFileReader(unittest.TestCase):

    @patch("pandas.read_csv")
    @patch("os.path.exists")
    def test_read_csv_file_success(self, mock_exists, mock_read_csv):
        """Тест успешного чтения CSV файла"""
        # Мокаем данные
        mock_exists.return_value = True
        mock_data = pd.DataFrame(
            [
                {"id": 1, "amount": 100, "currency": "USD", "date": "2023-01-01"},
                {"id": 2, "amount": 200, "currency": "EUR", "date": "2023-01-02"},
            ]
        )
        mock_read_csv.return_value = mock_data

        # Вызываем функцию
        result = read_csv_file("data/transactions.csv")

        # Проверяем результат
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["currency"], "EUR")
        mock_read_csv.assert_called_once_with("data/transactions.csv")

    @patch("pandas.read_csv")
    @patch("os.path.exists")
    def test_read_csv_file_empty(self, mock_exists, mock_read_csv):
        """Тест чтения пустого CSV файла"""
        mock_exists.return_value = True
        mock_read_csv.return_value = pd.DataFrame()

        result = read_csv_file("data/empty.csv")

        self.assertEqual(len(result), 0)
        mock_read_csv.assert_called_once_with("data/empty.csv")

    @patch("pandas.read_excel")
    @patch("os.path.exists")
    def test_read_excel_file_success(self, mock_exists, mock_read_excel):
        """Тест успешного чтения Excel файла"""
        mock_exists.return_value = True
        mock_data = pd.DataFrame(
            [
                {"id": 1, "amount": 150, "currency": "RUB", "date": "2023-01-03"},
                {"id": 2, "amount": 300, "currency": "USD", "date": "2023-01-04"},
            ]
        )
        mock_read_excel.return_value = mock_data

        result = read_excel_file("data/transactions_excel.xlsx")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["amount"], 150)
        self.assertEqual(result[1]["id"], 2)
        mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")

    @patch("os.path.exists")
    def test_read_csv_file_not_found(self, mock_exists):
        """Тест обработки отсутствующего CSV файла"""
        mock_exists.return_value = False

        with self.assertRaises(FileNotFoundError) as context:
            read_csv_file("data/nonexistent.csv")

        self.assertIn("CSV файл не найден", str(context.exception))

    @patch("os.path.exists")
    def test_read_excel_file_not_found(self, mock_exists):
        """Тест обработки отсутствующего Excel файла"""
        mock_exists.return_value = False

        with self.assertRaises(FileNotFoundError) as context:
            read_excel_file("data/nonexistent.xlsx")

        self.assertIn("Excel файл не найден", str(context.exception))

    @patch("pandas.read_csv")
    @patch("os.path.exists")
    def test_read_csv_file_exception(self, mock_exists, mock_read_csv):
        """Тест обработки исключения при чтении CSV"""
        mock_exists.return_value = True
        mock_read_csv.side_effect = Exception("Read error")

        with self.assertRaises(Exception) as context:
            read_csv_file("data/corrupted.csv")

        self.assertIn("Ошибка чтения CSV файла", str(context.exception))

    @patch("pandas.read_excel")
    @patch("os.path.exists")
    def test_read_excel_file_exception(self, mock_exists, mock_read_excel):
        """Тест обработки исключения при чтении Excel"""
        mock_exists.return_value = True
        mock_read_excel.side_effect = Exception("Read error")

        with self.assertRaises(Exception) as context:
            read_excel_file("data/corrupted.xlsx")

        self.assertIn("Ошибка чтения Excel файла", str(context.exception))


if __name__ == "__main__":
    unittest.main()
