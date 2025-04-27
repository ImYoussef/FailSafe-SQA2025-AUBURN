import unittest

from constants import (
    FORBIDDEN_PASS_NAMES,
    FORBIDDEN_USER_NAMES,
    INVALID_SECRET_CONFIG_VALUES,
    LEGIT_KEY_NAMES,
    SECRET_PASSWORD_LIST,
    SECRET_USER_LIST,
    VALID_KEY_STRING,
)
from scanner import isValidUserName


class UserNameFuzzer(unittest.TestCase):
    def setUp(self):
        # Test data using constants
        self.forbidden_usernames = FORBIDDEN_USER_NAMES
        self.secret_user_list = SECRET_USER_LIST
        self.secret_password_list = SECRET_PASSWORD_LIST
        self.forbidden_pass_names = FORBIDDEN_PASS_NAMES
        self.invalid_secret_values = INVALID_SECRET_CONFIG_VALUES
        self.legit_key_names = LEGIT_KEY_NAMES
        self.valid_key_strings = VALID_KEY_STRING

        # Generate variations of forbidden usernames
        self.forbidden_variations = []
        for name in self.forbidden_usernames:
            self.forbidden_variations.extend(
                [
                    name.upper(),
                    name.lower(),
                    name.capitalize(),
                    f"prefix_{name}",
                    f"{name}_suffix",
                    f"prefix_{name}_suffix",
                    f"123{name}456",
                    f"{name}@domain.com",
                    f"{name}.test",
                    f"{name}-test",
                ]
            )

        # Generate variations of secret user list
        self.secret_user_variations = []
        for name in self.secret_user_list:
            self.secret_user_variations.extend(
                [
                    name.upper(),
                    name.lower(),
                    name.capitalize(),
                    f"prefix_{name}",
                    f"{name}_suffix",
                    f"prefix_{name}_suffix",
                    f"123{name}456",
                    f"{name}@domain.com",
                    f"{name}.test",
                    f"{name}-test",
                ]
            )

    def test_forbidden_usernames(self):
        """Test with forbidden usernames from constants"""
        for username in self.forbidden_usernames:
            self.assertFalse(
                isValidUserName(username),
                f"Expected {username} to be invalid (forbidden username)",
            )

    def test_forbidden_variations(self):
        """Test with variations of forbidden usernames"""
        for username in self.forbidden_variations:
            try:
                result = isValidUserName(username)
                self.assertIsInstance(
                    result, bool, f"Expected boolean result for {username}"
                )
            except Exception as e:
                self.fail(f"Function crashed on input {username}: {str(e)}")

    def test_secret_user_list(self):
        """Test with secret user list from constants"""
        for username in self.secret_user_list:
            try:
                result = isValidUserName(username)
                self.assertIsInstance(
                    result, bool, f"Expected boolean result for {username}"
                )
            except Exception as e:
                self.fail(f"Function crashed on input {username}: {str(e)}")

    def test_secret_user_variations(self):
        """Test with variations of secret user list"""
        for username in self.secret_user_variations:
            try:
                result = isValidUserName(username)
                self.assertIsInstance(
                    result, bool, f"Expected boolean result for {username}"
                )
            except Exception as e:
                self.fail(f"Function crashed on input {username}: {str(e)}")

    def test_combined_constants(self):
        """Test with combinations of different constants"""
        test_cases = []

        # Combine forbidden usernames with secret user list
        for forbidden in self.forbidden_usernames:
            for secret in self.secret_user_list:
                test_cases.extend(
                    [
                        f"{forbidden}_{secret}",
                        f"{secret}_{forbidden}",
                        f"{forbidden}{secret}",
                        f"{secret}{forbidden}",
                    ]
                )

        # Combine with forbidden pass names
        for pass_name in self.forbidden_pass_names:
            test_cases.extend(
                [
                    f"user_{pass_name}",
                    f"{pass_name}_user",
                    f"admin_{pass_name}",
                    f"{pass_name}_admin",
                ]
            )

        # Combine with invalid secret values
        for invalid in self.invalid_secret_values:
            if isinstance(invalid, str):
                test_cases.extend(
                    [
                        f"user_{invalid}",
                        f"{invalid}_user",
                        f"admin_{invalid}",
                        f"{invalid}_admin",
                    ]
                )

        for username in test_cases:
            try:
                result = isValidUserName(username)
                self.assertIsInstance(
                    result, bool, f"Expected boolean result for {username}"
                )
            except Exception as e:
                self.fail(f"Function crashed on input {username}: {str(e)}")

    def test_edge_cases_with_constants(self):
        """Test edge cases using constants"""
        edge_cases = []

        # Empty and whitespace variations
        edge_cases.extend(["", " ", "\t", "\n", "  ", "\t\t", "\n\n"])

        # Combine with forbidden usernames
        for forbidden in self.forbidden_usernames:
            edge_cases.extend(
                [
                    f" {forbidden} ",
                    f"\t{forbidden}\t",
                    f"\n{forbidden}\n",
                    f"  {forbidden}  ",
                    f"\t\t{forbidden}\t\t",
                    f"\n\n{forbidden}\n\n",
                ]
            )

        # Combine with secret user list
        for secret in self.secret_user_list:
            edge_cases.extend(
                [
                    f" {secret} ",
                    f"\t{secret}\t",
                    f"\n{secret}\n",
                    f"  {secret}  ",
                    f"\t\t{secret}\t\t",
                    f"\n\n{secret}\n\n",
                ]
            )

        for username in edge_cases:
            try:
                result = isValidUserName(username)
                self.assertIsInstance(
                    result, bool, f"Expected boolean result for {username}"
                )
            except Exception as e:
                self.fail(f"Function crashed on input {username}: {str(e)}")


if __name__ == "__main__":
    unittest.main()
