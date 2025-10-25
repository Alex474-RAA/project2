import json
import os
import tempfile

from src.utils import load_json_data


def test_load_json_data_valid_file():
    """Тест загрузки корректного JSON-файла."""
    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(test_data, f)
        temp_path = f.name

    try:
        result = load_json_data(temp_path)
        assert result == test_data
    finally:
        os.unlink(temp_path)


def test_load_json_data_invalid_json():
    """Тест загрузки некорректного JSON-файла."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write("invalid json content")
        temp_path = f.name

    try:
        result = load_json_data(temp_path)
        assert result == []
    finally:
        os.unlink(temp_path)


def test_load_json_data_not_list():
    """Тест загрузки JSON-файла, который не содержит список."""
    test_data = {"id": 1, "amount": 100}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(test_data, f)
        temp_path = f.name

    try:
        result = load_json_data(temp_path)
        assert result == []
    finally:
        os.unlink(temp_path)


def test_load_json_data_file_not_found():
    """Тест загрузки несуществующего файла."""
    result = load_json_data("nonexistent_file.json")
    assert result == []
