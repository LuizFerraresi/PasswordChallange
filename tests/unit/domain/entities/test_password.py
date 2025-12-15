import pytest

from src.domain.entities.password import Password


@pytest.mark.parametrize("value, expected_result", [
    pytest.param("", False, id="empty password"),
    pytest.param("short", False, id="short password"),
    pytest.param("longenough", True, id="minimum lenght password"),
])
def test_password_validate_lenght(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validated_lenght()
    # assert
    assert result is expected_result

@pytest.mark.parametrize("value, expected_result", [
    pytest.param("password", False, id="no digit"),
    pytest.param("1", True, id="contains digit"),
])
def test_password_validate_digit(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validated_digit()
    # assert
    assert result is expected_result

@pytest.mark.parametrize("value, expected_result", [
    pytest.param("A", False, id="no lowercase letter"),
    pytest.param("a", True, id="contains lowercase letter"),
])
def test_password_validate_lowercase_letter(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validated_lowercase_letter()
    # assert
    assert result is expected_result

@pytest.mark.parametrize("value, expected_result", [
    pytest.param("a", False, id="no uppercase letter"),
    pytest.param("A", True, id="contains uppercase letter"),
])
def test_password_validate_uppercase_letter(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validated_uppercase_letter()
    # assert
    assert result is expected_result

@pytest.mark.parametrize("value, expected_result", [
    pytest.param("password", False, id="no special character"),
    pytest.param("!", True, id="exclamation mark"),
    pytest.param("@", True, id="at symbol"),
    pytest.param("#", True, id="hash"),
    pytest.param("$", True, id="dollar sign"),
    pytest.param("%", True, id="percent"),
    pytest.param("^", True, id="caret"),
    pytest.param("&", True, id="ampersand"),
    pytest.param("*", True, id="asterisk"),
    pytest.param("(", True, id="open parenthesis"),
    pytest.param(")", True, id="close parenthesis"),
    pytest.param("-", True, id="minus"),
    pytest.param("+", True, id="plus"),
])
def test_password_validate_special_character(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validated_special_character()
    # assert
    assert result is expected_result

@pytest.mark.parametrize("value, expected_result", [
    pytest.param("ab", True, id="no repeated characters"),
    pytest.param("Aa", True, id="lowercase and uppercase different"),
    pytest.param("aa", False, id="repeated lowercase characters"),
    pytest.param("AA", False, id="repeated uppercase characters"),
])
def test_password_validate_repeated_characters(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validated_repeated_characters()
    # assert
    assert result is expected_result

@pytest.mark.parametrize("value, expected_result", [
    pytest.param("password", True, id="no whitespace"),
    pytest.param("pass word", False, id="contains whitespace"),
])
def test_password_validate_whitespace(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validated_whitespace()
    # assert
    assert result is expected_result

@pytest.mark.parametrize("value, expected_result", [
    pytest.param("", False, id="empty string"),
    pytest.param("aa", False, id="repeated letter"),
    pytest.param("ab", False, id="no uppercase letter"),
    pytest.param("AAAbbbCc", False, id="no digit and special character"),
    pytest.param("AbTp9!foo", False, id="repeated lowercase letter"),
    pytest.param("AbTp9!foA", False, id="repeated uppercase letter"),
    pytest.param("AbTp9 fok", False, id="contains whitespace"),
    pytest.param("AbTp9!fok", True, id="valid password"),
])
def test_password_validate(value, expected_result):
    # arrange
    password = Password(value)
    # act
    result = password.validate()
    # assert
    assert result is expected_result
