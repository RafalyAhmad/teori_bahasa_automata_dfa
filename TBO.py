class PasswordDFA:
    def __init__(self):
        self.state = "START"
        self.transitions = {
            "START": self.start,
            "LENGTH": self.check_length,
            "NUMBER": self.check_number,
            "UPPER": self.check_upper,
            "SYMBOL": self.check_symbol,
            "VALID": self.valid_password,
            "INVALID": self.invalid_password,
        }

    def start(self, char):
        if char.isalnum():
            self.state = "LENGTH"
        elif char.isdigit():
            self.state = "NUMBER"
        elif char.isupper():
            self.state = "UPPER"
        elif not char.isalnum():
            self.state = "SYMBOL"
        else:
            self.state = "INVALID"

    def check_length(self, char):
        if len(self.password) >= 10:
            if char.isalnum():
                self.state = "LENGTH"
            elif char.isdigit():
                self.state = "NUMBER"
            elif char.isupper():
                self.state = "UPPER"
            elif not char.isalnum():
                self.state = "SYMBOL"
        else:
            self.state = "INVALID"

    def check_number(self, char):
        if char.isdigit():
            self.state = "NUMBER"
        elif char.isalnum():
            self.state = "LENGTH"
        elif char.isupper():
            self.state = "UPPER"
        elif not char.isalnum():
            self.state = "SYMBOL"
        else:
            self.state = "INVALID"

    def check_upper(self, char):
        if char.isupper():
            self.state = "UPPER"
        elif char.isdigit():
            self.state = "NUMBER"
        elif char.isalnum():
            self.state = "LENGTH"
        elif not char.isalnum():
            self.state = "SYMBOL"
        else:
            self.state = "INVALID"

    def check_symbol(self, char):
        if not char.isalnum():
            self.state = "SYMBOL"
        elif char.isdigit():
            self.state = "NUMBER"
        elif char.isalnum():
            self.state = "LENGTH"
        elif char.isupper():
            self.state = "UPPER"
        else:
            self.state = "INVALID"

    def valid_password(self):
        return True

    def invalid_password(self):
        return False

    def validate_password(self, password):
        self.password = password
        self.state = "START"

        try:
            for char in password:
                if self.state in self.transitions:
                    self.transitions[self.state](char)
                else:
                    self.state = "INVALID"
                    break

            if (
                len(password) >= 10
                and any(char.isdigit() for char in password)
                and any(char.isupper() for char in password)
                and any(not char.isalnum() for char in password)
            ):
                self.state = "VALID"
            else:
                self.state = "INVALID"

            return self.state == "VALID"

        except TypeError:
            print("Password invalid")

    def get_user_input_and_validate(self):
        password = input("Masukkan kata sandi Anda: ")
        if self.validate_password(password):
            print("Kata sandi valid!")
        else:
            print("Kata sandi tidak valid.")


# Contoh penggunaan
password_checker = PasswordDFA()
password_checker.get_user_input_and_validate()
