import tempfile

from src.decorators import log


def test_log_ok_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"
    assert result == 3


def test_log_exception_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    # result = my_function("1", 2)
    # captured = capsys.readouterr()
    assert """my_function error: can only concatenate str (not "int") to str Inputs: ('1', 2)"""


def test_log_ok_file(capsys):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):
        return x + y

    # result = my_function(1, 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "my_function ok" in logs


def test_log_exception_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):
        return x + y

    # result = my_function("1", 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert """my_function error: can only concatenate str (not "int") to str Inputs: ('1', 2)""" in logs
