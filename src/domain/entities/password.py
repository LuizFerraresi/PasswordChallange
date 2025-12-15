import re


class Password:
    def __init__(self, value: str) -> None:
        self._value = value
    
    def _search_with_regex(self, pattern: str) -> bool:
        """Helper method to search for a pattern in the password using regex."""
        return bool(re.search(pattern, self._value))

    def validated_lenght(self, min_length: int = 9) -> bool:
        """Validate if the password meets the minimum length requirement."""
        return len(self._value) >= min_length
    
    def validated_digit(self) -> bool:
        """Validate if the password contains at least one digit."""
        return self._search_with_regex(r'\d')
    
    def validated_lowercase_letter(self) -> bool:
        """Validate if the password contains at least one lowercase letter."""
        return self._search_with_regex(r'[a-z]')
        
    def validated_uppercase_letter(self) -> bool:
        """Validate if the password contains at least one uppercase letter."""
        return self._search_with_regex(r'[A-Z]')

    def validated_special_character(self) -> bool:
        """Validate if the password contains at least one special character."""
        return self._search_with_regex(r'[!@#$%^&*()\-+]')

    def validated_repeated_characters(self) -> bool:
        """Validate if the password contains no repeated characters."""
        return len(set(self._value)) == len(self._value)
    
    def validated_whitespace(self) -> bool:
        """Validate if the password contains no whitespace characters."""
        return not self._search_with_regex(r'\s')
    
    def validate(self) -> bool:
        return (
            self.validated_lenght() and
            self.validated_digit() and
            self.validated_lowercase_letter() and
            self.validated_uppercase_letter() and
            self.validated_special_character() and
            self.validated_repeated_characters() and
            self.validated_whitespace()
        )
