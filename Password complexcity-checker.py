import re


def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    specialchar_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or specialchar_error)

    if password_ok:
        return "Strong password! Good job."
    else:
        errors = []
        if length_error:
            errors.append("Password should be at least 8 characters long.")
        if digit_error:
            errors.append("Password should contain at least one digit.")
        if uppercase_error:
            errors.append("Password should contain at least one uppercase letter.")
        if lowercase_error:
            errors.append("Password should contain at least one lowercase letter.")
        if specialchar_error:
            errors.append("Password should contain at least one special character (e.g., !@#$%^&*()).")

        return "\n".join(errors)


def main():
    print("--- Password Strength Checker ---")
    while True:
        password = input("Enter your password: ")
        if not password:
            print("Please enter a password.")
            continue
        strength = check_password_strength(password)
        print(strength)
        if strength == "Strong password! Good job.":
            break


if __name__ == "__main__":
    main()
