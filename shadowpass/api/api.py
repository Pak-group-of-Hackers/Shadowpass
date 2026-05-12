from fastapi import FastAPI, HTTPException

from shadowpass.core.breach import HaveIBeenPwnedBreachChecker
from shadowpass.core.cracktime import CrackTimeEstimator
from shadowpass.core.entropy import calculate_entropy
from shadowpass.core.generator import PasswordGenerator
from shadowpass.core.hashgen import HashGenerator
from shadowpass.core.strength import PasswordStrengthAnalyzer

app = FastAPI(title="ShadowPass API", version="1.0.0")


@app.get("/analyze")
def analyze(password: str):
    if not password:
        raise HTTPException(status_code=400, detail="Password query parameter is required.")
    analyzer = PasswordStrengthAnalyzer()
    return analyzer.analyze_password(password)


@app.get("/entropy")
def entropy(password: str):
    if not password:
        raise HTTPException(status_code=400, detail="Password query parameter is required.")
    entropy_bits, pool_size = calculate_entropy(password)
    return {"entropy_bits": entropy_bits, "pool_size": pool_size}


@app.get("/cracktime")
def cracktime(password: str):
    if not password:
        raise HTTPException(status_code=400, detail="Password query parameter is required.")
    estimator = CrackTimeEstimator()
    return estimator.estimate(password)


@app.get("/generate")
def generate(
    length: int = 16,
    uppercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
    avoid_ambiguous: bool = True,
):
    generator = PasswordGenerator()
    return {
        "password": generator.generate(
            length=length,
            uppercase=uppercase,
            digits=digits,
            symbols=symbols,
            avoid_ambiguous=avoid_ambiguous,
        )
    }


@app.get("/hash")
def hash_password(value: str, rounds: int = 12):
    if not value:
        raise HTTPException(status_code=400, detail="Value query parameter is required.")
    hasher = HashGenerator()
    return {
        "md5": hasher.md5(value),
        "sha1": hasher.sha1(value),
        "sha256": hasher.sha256(value),
        "bcrypt": hasher.bcrypt_hash(value, rounds=rounds),
    }
