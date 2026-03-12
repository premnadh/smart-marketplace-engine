from pydantic import BaseModel, Field, EmailStr, field_validator
import re


class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=6,
        max_length=12,
        description="Username must be between 6 and 12 characters"
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        description="Password must include uppercase, lowercase, number, and special character"
    )

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).+$'
        if not re.match(pattern, value):
            raise ValueError(
                "Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character"
            )
        return value


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True