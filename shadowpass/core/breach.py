import hashlib
from typing import Tuple

import requests
from requests.exceptions import RequestException


class HaveIBeenPwnedBreachChecker:
    """Check password breaches using the Have I Been Pwned k-anonymity API."""

    API_URL = "https://api.pwnedpasswords.com/range/"
    HEADERS = {
        "User-Agent": "ShadowPass-Password-Security-Framework",
        "Add-Padding": "true",
    }

    def check_password(self, password: str) -> Tuple[int, str]:
        if not password:
            raise ValueError("Password cannot be empty.")

        sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        try:
            response = requests.get(
                f"{self.API_URL}{prefix}", headers=self.HEADERS, timeout=10
            )
            response.raise_for_status()
        except RequestException as exc:
            raise ConnectionError("Unable to query breach database.") from exc

        for line in response.text.splitlines():
            line_hash, count = line.split(":")
            if line_hash == suffix:
                return int(count), prefix

        return 0, prefix
