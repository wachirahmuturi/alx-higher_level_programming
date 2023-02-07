#!/usr/bin/python3
"""
Module 11-student
Contains class Student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that retrieves its dictionary representation
"""


class Student():
    """
    Public attributes : first_name, last_name, age
    Public methods: to_json (retrieves dict representation)
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with a 1st name and last name
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary
   
        Return:Only return dict of attrs given to us
        Return entire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

