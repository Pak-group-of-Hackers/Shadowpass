import re
from pathlib import Path
from typing import Dict, List

from zxcvbn import zxcvbn

COMMON_PASSWORDS_PATH = Path(__file__).resolve().parents[1] / "wordlists" / "common_passwords.txt"


class PasswordStrengthAnalyzer:
    """Analyze password characteristics and generate a strength report."""

    def __init__(self) -> None:
        self.common_passwords = self._load_common_passwords()

    def _load_common_passwords(self) -> List[str]:
        try:
            with COMMON_PASSWORDS_PATH.open("r", encoding="utf-8") as handle:
                return [line.strip() for line in handle if line.strip()]
        except FileNotFoundError:
            return []

    def _find_repeated_characters(self, password: str) -> int:
        repeats = re.findall(r"(.)\1{2,}", password)
        return len(repeats)

    def _find_sequences(self, password: str) -> int:
        password_lower = password.lower()
        sequence_count = 0
        alphabets = ["abcdefghijklmnopqrstuvwxyz", "0123456789"]
        for alphabet in alphabets:
            for index in range(len(alphabet) - 2):
                chunk = alphabet[index : index + 3]
                if chunk in password_lower or chunk[::-1] in password_lower:
                    sequence_count += 1
        return sequence_count

    def _is_common_password(self, password: str) -> bool:
        candidate = password.strip().lower()
        return candidate in self.common_passwords

    def analyze_password(self, password: str) -> Dict[str, object]:
        if not password:
            raise ValueError("Password cannot be empty.")

        length = len(password)
        upper = bool(re.search(r"[A-Z]", password))
        lower = bool(re.search(r"[a-z]", password))
        digits = bool(re.search(r"[0-9]", password))
        symbols = bool(re.search(r"[^A-Za-z0-9]", password))
        repeated = self._find_repeated_characters(password)
        sequences = self._find_sequences(password)
        common_password = self._is_common_password(password)

        score = 0
        score += 1 if length >= 8 else 0
        score += 1 if length >= 12 else 0
        score += 1 if length >= 16 else 0
        score += 1 if upper and lower else 0
        score += 1 if digits else 0
        score += 1 if symbols else 0
        score -= 1 if repeated else 0
        score -= 1 if sequences else 0
        score = max(score, 0)

        try:
            zxcvbn_result = zxcvbn(password)
            crack_score = zxcvbn_result.get("score", 0)
        except Exception:
            crack_score = 0

        if common_password or crack_score <= 1 or score <= 1:
            rating = "Weak"
        elif score <= 3 or crack_score == 2:
            rating = "Medium"
        elif score <= 5 or crack_score == 3:
            rating = "Strong"
        else:
            rating = "Very Strong"

        return {
            "password": password,
            "length": length,
            "has_uppercase": upper,
            "has_lowercase": lower,
            "has_digits": digits,
            "has_symbols": symbols,
            "repeated_sequences": repeated,
            "sequential_patterns": sequences,
            "common_password": common_password,
            "score": score,
            "zxcvbn_score": crack_score,
            "rating": rating,
        }
