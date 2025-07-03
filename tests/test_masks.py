import unittest
from src.masks import get_mask_card_number, get_mask_account  # Импортируйте ваши функции


class TestMaskFunctions(unittest.TestCase):
    # Тесты для маскировки карт
    def test_card_mask_normal(self):
        self.assertEqual(get_mask_card_number("7000792289606361"), "7000 79** **** 6361")

    def test_card_mask_with_spaces(self):
        self.assertEqual(get_mask_card_number("7000 7922 8960 6361"), "7000 79** **** 6361")

    def test_card_mask_short_number(self):
        with self.assertRaises(ValueError):
            get_mask_card_number("123456789012345")  # 15 цифр

    def test_card_mask_non_digits(self):
        with self.assertRaises(ValueError):
            get_mask_card_number("7000abcd89606361")

    # Тесты для маскировки счетов
    def test_account_mask_normal(self):
        self.assertEqual(get_mask_account("73654108430135874305"), "**4305")

    def test_account_mask_short(self):
        self.assertEqual(get_mask_account("1234"), "**1234")

    def test_account_mask_min_length(self):
        with self.assertRaises(ValueError):
            get_mask_account("123")  # Меньше 4 цифр

    def test_account_mask_with_spaces(self):
        self.assertEqual(get_mask_account("7365 4108 4301 3587 4305"), "**4305")

    def test_account_mask_non_digits(self):
        with self.assertRaises(ValueError):
            get_mask_account("acc4305")


if __name__ == "__main__":
    unittest.main()