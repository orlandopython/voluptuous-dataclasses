"""
Dataclass representing our test comments
"""

# library
from dataclasses import dataclass

@dataclass
class Comment:
    """
    A forum comment
    """
    id: int
    post_id: int
    email: str
    name: str
    body: str
    user_id: int
