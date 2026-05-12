import bcrypt
import hashlib


class HashGenerator:
    """Generate common cryptographic hashes for defensive password analysis."""

    @staticmethod
    def md5(value: str) -> str:
        if value is None:
            raise ValueError("Value cannot be None.")
        return hashlib.md5(value.encode("utf-8")).hexdigest()

    @staticmethod
    def sha1(value: str) -> str:
        if value is None:
            raise ValueError("Value cannot be None.")
        return hashlib.sha1(value.encode("utf-8")).hexdigest()

    @staticmethod
    def sha256(value: str) -> str:
        if value is None:
            raise ValueError("Value cannot be None.")
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    @staticmethod
    def bcrypt_hash(value: str, rounds: int = 12) -> str:
        if value is None:
            raise ValueError("Value cannot be None.")
        salted = bcrypt.gensalt(rounds=rounds)
        return bcrypt.hashpw(value.encode("utf-8"), salted).decode("utf-8")
