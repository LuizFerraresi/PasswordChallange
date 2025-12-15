from domain.entities.password import Password


class AuthService:
    def __init__(self) -> None:
        pass
    
    def validate_password(self, password: str) -> dict[str, bool]:
        valid = Password(password).validate()
        return {"valid": valid}
