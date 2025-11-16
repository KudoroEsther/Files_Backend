# Twitter Valiadation

from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import Optional

class TwitterUser(BaseModel):
    username: str = Field(..., min_length=3, max_length= 15)
    post: str
    account_type: str = Field(..., description="free or premium")

    @field_validator("username")
    def check_reserved_username(cls, v):
        if v.lower() in ["admin", "twitter"]:
            raise ValueError("Username is reserved and cannot be used.")
        
    @field_validator("account_type")
    def check_account_type(cls, v):
        if v.lower() not in ['free', 'premium']:
            raise ValueError("Account type must be 'free' or 'premium'.")
        return v.lower()
    
    @field_validator("post")
    def check_post_length(cls, v, values):
        account = values.get("account_type")
        if not account:
            return v
        
        max_len = 2800 if account == 'free' else 25000
        if len(v) > max_len:
            raise ValueError(f"{account.capitalize()} users can only post up to {max_len} characters.")
        return v

def test_users():
    print("Running validation test...")