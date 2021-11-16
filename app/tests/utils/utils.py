import time
import random
import string


def current_milli_time():
    return round(time.time() * 1000)


random.seed(current_milli_time())


def random_lower_string(num: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=num))


def random_int_number() -> int:
    return random.randint(0,3)