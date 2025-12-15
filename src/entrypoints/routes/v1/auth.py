from fastapi import APIRouter

from schemas.password import PasswordRequestSchema, PasswordResponseSchema
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    path="/password",
    response_model=PasswordResponseSchema,
)
def validate_password_route(payload: PasswordRequestSchema) -> dict[str, bool]:
    return AuthService().validate_password(payload.password)
