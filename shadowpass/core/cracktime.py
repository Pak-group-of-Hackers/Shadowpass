from typing import Dict

from .entropy import calculate_entropy


class CrackTimeEstimator:
    """Estimate password crack times based on entropy and dictionary attack speeds."""

    ATTACK_SPEEDS = {
        "online": 1000,
        "offline_fast_hashing": 10000000000,
        "offline_slow_hashing": 1000,
    }

    def estimate(self, password: str) -> Dict[str, object]:
        if not password:
            raise ValueError("Password cannot be empty.")

        entropy, _ = calculate_entropy(password)
        guesses = 2 ** min(entropy, 128)
        results = {}

        for label, speed in self.ATTACK_SPEEDS.items():
            seconds = guesses / speed
            results[label] = {
                "seconds": round(seconds, 2),
                "minutes": round(seconds / 60, 2),
                "hours": round(seconds / 3600, 2),
                "days": round(seconds / 86400, 2),
                "years": round(seconds / 31_536_000, 2),
            }

        results["entropy"] = entropy
        return results
