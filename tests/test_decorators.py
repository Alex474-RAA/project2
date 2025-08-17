import pytest

from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_success_file(tmp_path):
    logfile = tmp_path / "test.log"

    @log(filename=str(logfile))
    def multiply(a, b):
        return a * b

    assert multiply(3, 4) == 12
    with open(logfile, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "multiply ok" in content


def test_log_error_file(tmp_path):
    logfile = tmp_path / "test.log"

    @log(filename=str(logfile))
    def fail_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail_func()

    with open(logfile, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "fail_func error: ValueError" in content
    assert "Inputs: (), {}" in content
