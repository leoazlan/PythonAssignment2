"""
place.py
Created on 25/09/2023

This module contains the Place class which represents a place to visit. It includes
attributes such as name, country, priority, and visited status, and methods to handle these
attributes.

Github URL: [https://github.com/JCUS-CP1404/cp1404-travel-tracker-assignment-2-leoazlan]
"""

class Place:
    # Class variable to indicate a place is unvisited
    UNVISITED = False

    def __init__(self, name="", country="", priority=0, visited=UNVISITED):
        """
        Constructor for the Place class. If no arguments are given,
        it initializes an "empty" place.
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        """
        Overrides the default __str__ method, to give a more meaningful string
        representation of a Place object.
        """
        return f"{self.name}, {self.country}, {self.priority}, {self.visited}"

    def mark_as_visited(self):
        """
        Marks a place as visited.
        """
        self.visited = True

    def mark_as_unvisited(self):
        """
        Marks a place as unvisited.
        """
        self.visited = False

    def is_important(self):
        """
        Checks if a place is important, defined as having a priority less than
        or equal to 2.
        """
        return self.priority <= 2