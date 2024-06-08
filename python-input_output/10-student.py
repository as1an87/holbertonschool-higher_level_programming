#!/usr/bin/python3
"""
class
"""


class Student:
    """
    A class that defines a student by:

    Public instance attributes:
    - first_name
    - last_name
    - age

    Instantiation with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Parameters:
        - attrs (list, optional): List of attribute names to retrieve.

        Returns:
        dict: A dictionary representation of the student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
