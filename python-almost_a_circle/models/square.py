#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """start class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"
