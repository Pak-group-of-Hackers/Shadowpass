🔐 ShadowPass – Advanced Password Security Framework

ShadowPass is a terminal-based password security framework designed for Kali Linux.
It focuses on defensive cybersecurity, password strength analysis, entropy calculation, breach detection, and secure password generation.

⚠️ Built strictly for educational and defensive security purposes only.

⚡ Overview

ShadowPass provides a hacker-style CLI experience inspired by tools like Metasploit and Nmap, but focused only on password security auditing and analysis.

🚨 Disclaimer

This tool is strictly for:

✅ Ethical cybersecurity learning
✅ Password strength analysis
✅ Defensive security research

It does NOT support:

❌ Hacking or unauthorized access
❌ Brute-force attacks
❌ Phishing or malware
❌ Any illegal activity

Any misuse is strictly prohibited.

🧠 Features
🔍 Password Strength Analysis
Length evaluation
Uppercase / lowercase detection
Numbers & symbols check
Pattern recognition
Common password detection
Output classification: Weak / Medium / Strong / Very Strong
📊 Entropy Calculator

Calculates password entropy using:

H=L×log
2
	​

(N)
Provides security strength in bits
Higher entropy = stronger password
⏱ Crack Time Estimator

Estimates brute-force resistance:

Seconds → Minutes → Years
Real-world attack simulation approximation
🧪 Breached Password Detection
Uses HaveIBeenPwned API (k-anonymity model)
Secure SHA-1 partial hash lookup
Shows breach count safely (no plain password exposure)
🔐 Password Generator

Custom secure password generator:

Adjustable length
Include/exclude symbols, numbers, uppercase
Avoids ambiguous characters
🔑 Hash Generator

Supports:

MD5
SHA1
SHA256
bcrypt
🎨 UI Design

ShadowPass includes a cyberpunk-style terminal interface:

Neon green hacker-style theme
ASCII startup banner
Animated loading screens
Structured logging system
📂 Project Structure
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
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
⚙️ Installation (Kali Linux)
1. Clone Repository
git clone https://github.com/Pak-group-of-Hackers/Shadowpass.git
cd Shadowpass
2. Install Dependencies
pip install -r requirements.txt
3. Run Tool
python main.py
📦 Requirements
rich
pyfiglet
colorama
requests
bcrypt
zxcvbn
fastapi
uvicorn
🖥️ Usage Menu
[1] Analyze Password
[2] Entropy Calculator
[3] Crack Time Estimator
[4] Breach Check
[5] Password Generator
[6] Hash Generator
[7] About
[8] Exit
🔥 Example Output
PASSWORD ANALYSIS RESULT
--------------------------------
Strength   : STRONG
Entropy    : 62.4 bits
Crack Time : 5,000 years
Status     : SAFE
🚀 Future Improvements
GUI version (Tkinter / Web UI)
AI-based password risk scoring
Cloud API mode
Advanced breach intelligence (defensive research only)
👨‍💻 Author

Pak Group of Hackers
Cybersecurity Research Division

⭐ Support

If you like this project:

⭐ Star the repository
🔁 Share with cybersecurity learners
🛠️ Contribute improvements
⚠️ Legal Notice

This project is strictly for ethical cybersecurity research and education only.
Any illegal use is not the responsibility of the developer.
