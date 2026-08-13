from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = "annotator"


class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
    role: str

    model_config = {
        "from_attributes": True
    }