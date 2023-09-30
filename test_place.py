"""Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.visited

    # Test mark_as_visited
    print("Test mark_as_visited:")
    new_place.mark_as_visited()
    print(new_place)
    assert new_place.visited

    # Test mark_as_unvisited
    print("Test mark_as_unvisited:")
    new_place.mark_as_unvisited()
    print(new_place)
    assert not new_place.visited

    # Test is_important
    print("Test is_important:")
    assert new_place.is_important()

    # Test is_important with priority more than 2
    print("Test is_important with priority more than 2:")
    new_place.priority = 3
    assert not new_place.is_important()


run_tests()