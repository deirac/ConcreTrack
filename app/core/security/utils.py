from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.core.config import get_settings

import bcrypt

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        get_settings().SECRET_KEY, 
        algorithm=get_settings().ALGORITHM
    )
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Convert the plain text password to bytes and truncate to 72 bytes
    encoded_password = plain_password.encode('utf-8')[:72]
    # Convert the stored hash from string to bytes
    stored_hash = hashed_password.encode('utf-8')
    try:
        return bcrypt.checkpw(encoded_password, stored_hash)
    except ValueError:
        return False

def get_password_hash(password: str) -> str:
    # Convert the password to bytes and truncate to 72 bytes
    encoded_password = password.encode('utf-8')[:72]
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded_password, salt)
    # Return the hash as a string
    return hashed.decode('utf-8')