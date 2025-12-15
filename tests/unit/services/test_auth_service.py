from unittest.mock import patch

from src.services.auth import AuthService


def test_password_service_validation():
    # arrange
    value = "password"
    service = AuthService()
    # act
    with patch('src.services.auth.Password') as password_cls_mock:
        password_instance = password_cls_mock.return_value
        password_instance.validate.return_value = True
        result = service.validate_password(value)

    # assert
    password_cls_mock.assert_called_once_with(value)
    password_instance.validate.assert_called_once()
    assert result == {"valid": True}
