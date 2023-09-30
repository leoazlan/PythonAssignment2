import os
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    new_place = Place("Smithfield", "Australia", 5, False)
    place_collection.add_place(new_place)
    assert new_place in place_collection.places

    # Test get_number_of_unvisited_places
    print("Test get_number_of_unvisited_places:")
    num_unvisited = place_collection.get_number_of_unvisited_places()
    print(f"Number of unvisited places: {num_unvisited}")
    assert num_unvisited == sum([1 for place in place_collection.places if place.visited == Place.UNVISITED])

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    sorted_places = sorted(place_collection.places, key=lambda x: x.priority)
    assert place_collection.places == sorted_places

    # Test saving places (check CSV file manually to see results)
    print("Test saving places:")
    place_collection.save_places()
    assert os.path.exists('places.csv')  # checks that the file exists

run_tests()