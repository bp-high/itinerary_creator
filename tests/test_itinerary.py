import pytest
from itinerary_creator.itinerary import find_all_itineraries, process_input


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("(New York -> Beijing), (Beijing -> Tokyo), (Tokyo -> Sydney)", ["New York -> Beijing -> Tokyo -> Sydney"]),
        ("(New York -> Beijing), (Beijing -> New York), (New York -> Tokyo), (Tokyo -> Sydney)",
         "Invalid or circular flight list"),
        ("(New York -> Beijing), (London -> Paris), (Beijing -> Tokyo)", sorted(["New York -> Beijing -> Tokyo",
                                                                                 "London -> Paris"])),
        ("", "Empty input"),
        ("(New York -> Beijing)", ["New York -> Beijing"]),
    ]
)
def test_itineraries(input_str, expected):
    flights = process_input(input_str)
    itineraries = find_all_itineraries(flights)
    print(itineraries)
    assert sorted(itineraries) == sorted(expected)
