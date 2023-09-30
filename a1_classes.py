

# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class


"""
Replace the contents of this module docstring with your own details
Name:Mohamed Azlan
Date started:20/04/2023
GitHub URL:https://github.com/JCUS-CP1404/cp1404-travel-tracker-assignment-2-leoazlan
"""


import csv
import random


FILENAME = "places.csv"


def load_places():
    """
    Load places from file and return as list of dictionaries

    Returns:
    List of dictionaries containing place information (name, country, priority, visited)
    """
    places = []
    try:
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["priority"] = int(row["priority"])
                row["visited"] = row["visited"] == "v"
                places.append(row)
    except FileNotFoundError:
        pass
    return places


def save_places(places):
    """
    Save places to file

    Args:
    places: List of dictionaries containing place information (name, country, priority, visited)
    """
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["name", "country", "priority", "visited"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for place in places:
            writer.writerow(place)


def list_places(places):
    """
    List all places, marking visited places with an asterisk

    Args:
    places: List of dictionaries containing place information (name, country, priority, visited)
    """
    num_unvisited = sum(1 for place in places if not place["visited"])
    for i, place in enumerate(places, start=1):
        visited = "*" if place["visited"] else ""
        print(f"{visited}{i}. {place['name']} in {place['country']} {place['priority']}")
    print(f"{len(places)} places. You still want to visit {num_unvisited} places.")


def recommend_place(places):
    """
    Recommend a random unvisited place

    Args:
    places: List of dictionaries containing place information (name, country, priority, visited)
    """
    unvisited_places = [place for place in places if not place["visited"]]
    if not unvisited_places:
        print("No places left to visit!")
    else:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {place['name']} in {place['country']}?")


def add_place(places):
    """
    Prompt user to add a new place to the list

    Args:
    places: List of dictionaries containing place information (name, country, priority, visited)
    """
    name = input("Name: ").strip()
    while not name:
        print("Input can not be blank")
        name = input("Name: ").strip()
    country = input("Country: ").strip()
    while not country:
        print("Input can not be blank")
        country = input("Country: ").strip()
    try:
        priority = int(input("Priority: "))
        if priority < 1:
            raise ValueError("Priority must be greater than zero")
    except ValueError as e:
        print(f"Invalid input; {e}")
        return

    places.append({"name": name, "country": country, "priority": priority, "visited": False})
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_visited(places):
    """
    Prompt user to mark a place as visited

    Args:
    places: List of dictionaries containing place information (name, country, priority, visited)
    """
    unvisited_places = [i for i, place in enumerate(places, start=1) if not place["visited"]]
    visited_places = [i for i, place in enumerate(places, start=1) if place["visited"]]
    if not unvisited_places:
        print("No unvisited places")
    else:
        print("* indicates unvisited")
        list_places(places)
        try:
            choice = int(input("Enter the number of a place to mark as visited\n"))
        except ValueError:
            print("Invalid input; enter a valid number")
            return
        if choice not in unvisited_places and choice not in visited_places:
            print("Invalid place number")
        elif choice in visited_places:
            print(f"You have already visited {places[choice-1]['name']}")
        else:
            places[choice-1]["visited"] = True
            print(f"{places[choice-1]['name']} visited!")


def main():
    """
    Main function that handles the user interface and manages the list of places
    """
    import random

    # Get user's name
    name = input("Enter your name: ")

    # Load saved places from file
    places = load_places()

    # Greet the user
    print("Welcome,", name, "to the travel tracker!")
    print("Travel Tracker 1.0 - by", name)
    print(f"{len(places)} places loaded from {FILENAME}")

    while True:
        print("Menu:")
        print("L - List places")
        print("R - Recommend random place")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")
        choice = input(">>> ").upper()

        if choice == "L":
            list_places(places)
        elif choice == "R":
            recommend_place(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_visited(places)
        elif choice == "Q":
            save_places(places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day...")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()
