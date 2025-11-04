from enum import Enum


class Role(str, Enum):
    super = "super"
    admin = "admin"
    operator = "operator"
    client = "client"
