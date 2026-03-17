import pytest
from app.core.security.utils import get_password_hash, verify_password

def test_password_hashing_and_verification():
    # Test normal password
    password = "normalpassword123"
    hashed = get_password_hash(password)
    assert verify_password(password, hashed)
    assert not verify_password("wrongpassword", hashed)

def test_long_password_handling():
    # Test password longer than 72 bytes
    long_password = "x" * 100
    hashed = get_password_hash(long_password)
    
    # Should still verify with full password
    assert verify_password(long_password, hashed)
    
    # Should not verify with wrong password of same length
    wrong_long_password = "y" * 100
    assert not verify_password(wrong_long_password, hashed)

def test_unicode_password_handling():
    # Test password with unicode characters
    unicode_password = "пароль123"  # Russian characters + numbers
    hashed = get_password_hash(unicode_password)
    assert verify_password(unicode_password, hashed)
    assert not verify_password("wrong" + unicode_password, hashed)

def test_special_characters_handling():
    # Test password with special characters
    special_password = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    hashed = get_password_hash(special_password)
    assert verify_password(special_password, hashed)
    assert not verify_password("wrong" + special_password, hashed)