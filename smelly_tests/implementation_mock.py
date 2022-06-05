def increment(n):
    return n + 1


def decrement(n):
    return n - 1


def increment_integer(n: int):
    if not isinstance(n, int):
        raise Exception('The input parameter should be an integer')
    return n + 1
