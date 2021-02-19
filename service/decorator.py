import time


def validate_parameter(func):
    def one_param_func(n):
        if n <= 0:
            return ConnectionAbortedError()

        return func(n)

    return one_param_func


def timing(func):
    def wrapper(*args):
        t0 = time.time()
        res = func(*args)
        t1 = time.time()
        print(f"It took {t1 - t0} seconds to execute")
        return res

    return wrapper
