from typing import List, Tuple
from collections import defaultdict


def format_city_name(city_name: str) -> str:
    """
    Inserts spaces in a city name before a capital letter if it is directly
    followed by a lowercase letter, assuming it's a concatenated city name.
    Example: 'NewYork' becomes 'New York'
    """
    formatted_name = ''.join(' ' + char if char.isupper() and i > 0 and city_name[i-1].islower() else char
                             for i, char in enumerate(city_name)).strip()
    return formatted_name


def find_itinerary(flights: List[Tuple[str, str]]) -> None:
    """
    This function prints the itinerary given a list of tuple which are the (departure,arrival) available.

    :param flights: List of tuples, where each tuple represents a flight (departure, arrival)
    :return: None, prints the itinerary
    """
    # Create a map to store the departure to arrival mapping
    flight_map = {departure: arrival for departure, arrival in flights}

    # Find the starting point: a city not present in arrivals
    start = None
    arrivals = set(flight_map.values())
    for departure in flight_map.keys():
        if departure not in arrivals:
            start = departure
            break

    # If no starting point print that the flight list is invalid
    # For cases where the given set of flights that start and end at the same city
    # (e.g., (New York -> Delhi), (Delhi -> New York)) , we would get this error

    #
    if start is None:
        print("Invalid flight list")
        return

    # Construct the itinerary by following the flight map
    itinerary = [start]
    while start in flight_map:
        next_stop = flight_map[start]
        itinerary.append(next_stop)
        start = next_stop

    # Print the itinerary
    print(" -> ".join(itinerary))


# For the test case where we have disconnected flights as input like (SF->Redmond), (New York->DC)
# our original function does not work, so we modify it a little"""
def find_all_itineraries(flights: List[Tuple[str, str]] | None) -> List[str] | str:
    """
    This function prints all itineraries given a list of tuples which are the (departure,arrival) available,
    handling disconnected flights.

    :param flights: List of tuples, where each tuple represents a flight (departure, arrival)
    :return: None, prints the itineraries
    """
    # Check of flights is None or not
    if flights is None:
        return "Empty input"

    # Create a map to store the departure to arrival mapping
    flight_map = defaultdict(list)
    for departure, arrival in flights:
        flight_map[departure].append(arrival)

    # Find all starting points: cities not present in arrivals
    all_cities = {city for flight in flights for city in flight}
    arrivals = {arrival for _, arrival in flights}
    starts = all_cities - arrivals

    # If no starting point found, the flight list might be circular or invalid
    if not starts:
        print("Invalid or circular flight list")
        return "Invalid or circular flight list"

    def construct_itinerary(start: str) -> List[str]:
        """
        Constructs an itinerary starting from the given city.

        :param start: The starting city
        :return: A list representing the itinerary
        """
        itinerary = [start]
        while flight_map[start]:
            next_stop = flight_map[start].pop(0)  # Remove the flight from map
            itinerary.append(next_stop)
            start = next_stop
        return itinerary

    # Construct and print all itineraries
    final_list = []
    for start in starts:
        itinerary = construct_itinerary(start)
        print(" -> ".join(format_city_name(city) for city in itinerary))
        final_list.append(" -> ".join(format_city_name(city) for city in itinerary))

    return sorted(final_list)


def process_input(input_str: str) -> List[Tuple[str, str]] | None:
    """
    This function takes the input given the format suggested in the problem and converts it into the List of tuple

    :param input_str: String containing flights in the format (City1 -> City2), ...
    :return: List of tuples, where each tuple represents a flight (departure, arrival)
    """
    # Handles the case when we are given empty input
    if input_str == "":
        print("Warning: Empty output")
        return None

    # Remove spaces, parentheses, and split by "),("
    flights_raw = input_str.replace(" ", "").strip()[1:-1].split("),(")

    # Split each item by "->" and convert to tuple
    flights = [tuple(flight.split("->")) for flight in flights_raw]

    return flights


# if __name__ == "__main__":
#     input_str = input("Enter flights: ")
#     flights = process_input(input_str=input_str)
#     # find_itinerary(flights=flights)
#     find_all_itineraries(flights=flights)
