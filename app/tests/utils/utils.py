import random
import string

from fastapi.testclient import TestClient


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def random_int_number() -> int:
    return random.randint(0,3)