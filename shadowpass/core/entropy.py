import math
from typing import Tuple


def calculate_entropy(password: str) -> Tuple[float, int]:
    """Calculate entropy in bits for a given password."""
    if not password:
        return 0.0, 0

    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(not char.isalnum() for char in password):
        charset_size += 32

    if charset_size == 0:
        return 0.0, 0

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2), charset_size
