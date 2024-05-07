#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state in the system.
    """

    def __init__(self):
        """
        Initializes a new instance of State.
        """
        super().__init__()
        self.name = ""
