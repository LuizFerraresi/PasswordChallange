from pydantic import BaseModel, Field


class PasswordRequestSchema(BaseModel):
    password: str =  Field(...)


class PasswordResponseSchema(BaseModel):
    valid: bool = Field(...)
