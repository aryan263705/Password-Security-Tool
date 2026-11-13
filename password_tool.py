import re
import secrets
import string

COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "admin", "welcome", "abc123",
}


def check_password_strength(password: str) -> tuple[int, str, list[str]]:
    """Return a simple strength score, rating, and improvement suggestions."""
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters; 12 or more is better.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number (0-9).")

    if re.search(r"""[!@#$%^&*(),.?":{}|<>_\\-]""", password):
        score += 1
    else:
        suggestions.append("Add a special character (for example: @, #, or $).")

    if password.casefold() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("This is a commonly used password. Choose a unique one.")

    if score <= 2:
        rating = "WEAK"
    elif score <= 4:
        rating = "MEDIUM"
    else:
        rating = "STRONG"

    return score, rating, suggestions


def generate_password(length: int = 14) -> str:
    """Generate a password using Python's cryptographically secure secrets module."""
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:
    while True:
        print("\n=== Password Security Tool ===")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            password = input("Enter password to check: ")
            score, rating, tips = check_password_strength(password)
            print(f"\nScore: {score}/6")
            print(f"Strength: {rating}")
            if tips:
                print("Suggestions:")
                for tip in tips:
                    print(f" - {tip}")

        elif choice == "2":
            try:
                length = int(input("Desired password length: "))
                generated = generate_password(length)
                print("Generated password:", generated)
                print("Store it in a trusted password manager.")
            except ValueError as error:
                print(f"Invalid input: {error}")

        elif choice == "3":
            print("Bye! Stay secure.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
