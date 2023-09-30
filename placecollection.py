import csv
from operator import attrgetter

"""
placecollection.py
Created on 10th June 2023

This module contains the PlaceCollection class which represents a collection of places. 
It includes methods to handle the loading and saving of the places from/to a CSV file, 
sorting of the places, adding a place to the collection, and getting the number of unvisited places.

Github URL: [https://github.com/JCUS-CP1404/cp1404-travel-tracker-assignment-2-leoazlan]
"""

import csv
from place import Place


class PlaceCollection:
    def __init__(self):
        """
        Constructor for the PlaceCollection class. Initializes an empty list of places.
        """
        self.places = []

    def load_places(self, filename):
        """
        Loads places from a CSV file. Each line of the CSV file is treated as a separate place.
        """
        with open(filename, 'r') as file:
            for line in file:
                name, country, priority, visited = line.strip().split(',')
                self.places.append(Place(name, country, int(priority), visited))

    def save_places(self):
        """
        Saves places to a CSV file. Each place is written as a separate line in the CSV file.
        """
        with open('./places.csv', mode='w', encoding='utf-8', newline="") as f:
            writer = csv.writer(f)
            writer.writerows([[i.name, i.country, i.priority, i.visited] for i in self.places])

    def add_place(self, place):
        """
        Adds a new place to the place collection.
        """
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        """
        Returns the number of places that are marked as unvisited.
        """
        return sum(1 for place in self.places if place.visited == Place.UNVISITED)

    def sort(self, attr_name):
        """
        Sorts the places in the collection based on a given attribute name.
        """
        self.places.sort(key=lambda k: getattr(k, attr_name))


