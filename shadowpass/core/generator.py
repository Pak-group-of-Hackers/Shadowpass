import secrets
import string
from typing import Optional


class PasswordGenerator:
    """Generate secure passwords with configurable character sets."""

    AMBIGUOUS = set("O0oIl1|`'\"/\\")

    def generate(
        self,
        length: int = 16,
        uppercase: bool = True,
        digits: bool = True,
        symbols: bool = True,
        avoid_ambiguous: bool = True,
    ) -> str:
        if length < 4:
            raise ValueError("Password length must be at least 4.")

        charset = []
        if uppercase:
            charset.extend(string.ascii_uppercase)
        if digits:
            charset.extend(string.digits)
        if symbols:
            charset.extend("!@#$%^&*()-_=+[]{}<>?" )
        charset.extend(string.ascii_lowercase)

        if not charset:
            raise ValueError("Character set cannot be empty.")

        if avoid_ambiguous:
            charset = [c for c in charset if c not in self.AMBIGUOUS]

        if not charset:
            raise ValueError("Character set was reduced to empty after removing ambiguous characters.")

        password_chars = [secrets.choice(string.ascii_lowercase)]
        if uppercase:
            password_chars.append(secrets.choice(string.ascii_uppercase))
        if digits:
            password_chars.append(secrets.choice(string.digits))
        if symbols:
            password_chars.append(secrets.choice("!@#$%^&*()-_=+[]{}<>?"))

        while len(password_chars) < length:
            password_chars.append(secrets.choice(charset))

        secrets.SystemRandom().shuffle(password_chars)
        return "".join(password_chars[:length])
