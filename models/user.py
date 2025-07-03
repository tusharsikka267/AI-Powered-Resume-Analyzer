from dataclasses import dataclass
from bson.objectid import ObjectId

@dataclass
class User:
    _id: ObjectId
    email: str
    password_hash: str
    created_at: str
