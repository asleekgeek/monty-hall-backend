from time import time


def validate_parameter(func):
    def one_param_func(n):
        if n <= 0:
            abort(406, "Negative values are not allowed")
        if n > 0:
            return func(n)

    return one_param_func


def timing(func):
    def wrapper(*args):
        t0 = time.time()
        res = func(*args)
        t1 = time.time()
        print("It took {} seconds to execute".format(t1 - t0))
        return res

    return wrapper
