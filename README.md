# ShadowPass

ShadowPass is a professional defensive password security framework inspired by Kali Linux tooling and cyberpunk terminal aesthetics. It is built to run on Kali Linux and other Linux distributions with Python 3, offering secure password analysis, entropy measurement, breach detection, password generation, and hashing features.

## Features

- Password strength analysis with metrics for length, uppercase, lowercase, digits, symbols, repeats, sequences, and common passwords.
- Entropy calculator with bit-level analysis.
- Crack time estimation for online and offline attacks using realistic speeds.
- Breached password detection using Have I Been Pwned k-anonymity API.
- Secure password generator with custom length, symbol/digit toggles, uppercase options, and ambiguous character avoidance.
- Hash generator for MD5, SHA1, SHA256, and bcrypt.
- Professional Kali-inspired terminal UI with animated startup, neon green theme, panels, and hacker-style banners.
- Optional FastAPI endpoint mode for integration.

## Kali Linux Setup

1. Open a terminal on Kali Linux.
2. Install Python 3 and pip if not already installed:

```bash
sudo apt update
sudo apt install -y python3 python3-pip
```

3. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Installation

Clone or copy the `shadowpass` project folder into your Kali Linux workspace.

```bash
cd /path/to/project
python3 -m pip install -r requirements.txt
```

## Usage

Run the terminal application from the project root:

```bash
python main.py
```

This launches the ShadowPass terminal UI with the interactive menu.

### Optional API Mode

Run the API server using uvicorn:

```bash
uvicorn shadowpass.api.api:app --reload --host 0.0.0.0 --port 8000
```

Example API request:

```bash
curl "http://127.0.0.1:8000/analyze?password=MyS3cureP@ss"
```

## Command Examples

- Analyze a password interactively: `python main.py`
- Start API server: `uvicorn shadowpass.api.api:app --reload`

## Project Structure

```text
shadowpass/
│
├── core/
│   ├── strength.py
│   ├── entropy.py
│   ├── cracktime.py
│   ├── breach.py
│   ├── generator.py
│   └── hashgen.py
│
├── ui/
│   ├── banner.py
│   ├── menu.py
│   └── animations.py
│
├── api/
│   └── api.py
│
├── assets/
├── reports/
├── wordlists/
│   └── common_passwords.txt
├── tests/
│   └── test_core.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Screenshots

> Add your terminal screenshots here once the application is running.

## Disclaimer

ShadowPass is intended only for defensive security use, password hygiene improvement, and research. It must not be used for unauthorized access, brute-force attacks, credential stuffing, phishing, malware, or any illegal activity.

## License

This project is provided for defensive cybersecurity and analysis purposes.
