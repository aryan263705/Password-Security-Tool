# Password Security Tool 🔐

A beginner-friendly Python command-line project that checks password strength and generates random passwords using Python's built-in `secrets` module.

## Features

- Checks password length and character variety.
- Gives a simple strength score (out of 6): **WEAK**, **MEDIUM**, or **STRONG**.
- Provides suggestions to improve a password.
- Flags a small set of commonly used passwords.
- Generates random passwords with a cryptographically secure random source.
- No third-party Python packages required.

## Project Structure

```text
Password-Security-Tool/
├── password_tool.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.10 or later
- No external dependencies

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/aryan263705/Password-Security-Tool.git
   cd Password-Security-Tool
   ```

2. Run the program:

   ```bash
   python password_tool.py
   ```

   On some systems, use `python3 password_tool.py`.

## Usage

Choose an option from the menu:

1. **Check password strength** – enter a password to receive a score, rating, and suggestions.
2. **Generate a strong password** – enter a length of at least 8 characters.
3. **Exit** – close the program.

## How the Score Works

| Check | Points |
|---|---:|
| 8–11 characters | 1 |
| 12 or more characters | 2 |
| Uppercase letter | 1 |
| Lowercase letter | 1 |
| Number | 1 |
| Special character | 1 |
| **Maximum** | **6** |

A few common passwords are assigned a zero score. This is an educational heuristic, not a complete password-security assessment.

## Security Notes

- The generator uses Python's `secrets` module rather than the predictable `random` module.
- The strength checker is a basic learning tool. It does not check breached-password databases, password reuse, or resistance to sophisticated guessing.
- Avoid entering real or currently used passwords into demonstration tools, especially on shared computers.
- Use a reputable password manager and enable multi-factor authentication where available.

## Author

**aryan263705**

---

⭐ Suggestions and improvements are welcome!
