from dataclasses import dataclass
from bson.objectid import ObjectId

@dataclass
class Job:
    _id: ObjectId
    title: str
    description: str
    company: str
    posted_at: str
