#!/usr/bin/python3
"""Module for User class."""

from models.base_models import Basemodel

class User(Basemodel):
    """Class representing a User."""
    emal = ""
    password = ""
    first_name = ""
    last_name = ""
