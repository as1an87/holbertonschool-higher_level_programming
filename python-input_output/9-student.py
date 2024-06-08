#!/usr/bin/python3
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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
        dict: A dictionary representation of the student instance.
        """
        return self.__dict__
