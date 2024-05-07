#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in the system.
    """

    def __init__(self):
        """
        Initializes a new instance of User.
        """
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
