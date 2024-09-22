import os


def log(filename=None):
    "Декоратор, который логирует вызов функции и ее результат в файл или консоль"

    def wrapper(function):
        # @wraps(function)
        def inner(*args, **kwargs):
            result = None
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                log_str = f"{function.__name__} error: {e} Inputs: {args}\n"
            else:
                log_str = f"{function.__name__} ok\n"
            finally:
                if filename:
                    path_to_file = os.path.join(os.path.dirname(__file__), "../logs", filename)
                    with open(path_to_file, "w", encoding="utf-8") as file:
                        file.write(log_str)
                    # with open(filename, "a") as file:
                    #     file.write(log_str)
                else:
                    print(log_str)
            return result

        return inner

    return wrapper


# @log()
# def my_function(x, y):
#     return x + y
#
# my_function("1", 2)


@log(filename="mylog.txt")
def my_function(x, y):
    "Функция которая выдает сумму сложения двух чисел"
    return x + y


my_function(1, 2)
