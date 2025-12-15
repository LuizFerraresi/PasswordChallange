import pytest
from starlette.status import HTTP_200_OK


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
def test_password_validate_route(value, expected_result, test_client):
    # arrange
    payload = {"password": value}
    # act
    response = test_client.post("/v1/auth/password", json=payload)
    # assert
    assert response.status_code == HTTP_200_OK
    assert response.json()['valid'] is expected_result
