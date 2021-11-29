"""Starter code for CSC108 Assignment 3"""

from typing import List, Set, Tuple
from flight_reader import AirportDict, RouteDict, AIRPORT_DATA_INDEXES

def get_airport_info(airports: AirportDict, iata: str, info: str) -> str:
    """Return the airport information for airport with IATA code iata for
    column info from AIRPORT_DATA_INDEXES.

    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name')
    'Apt1'
    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA4', 'IATA')
    'AA4'
    """

    # Complete the function body

    return airports[iata][AIRPORT_DATA_INDEXES[info]]

def is_direct_flight(iata_src: str, iata_dst: str, routes: RouteDict) -> bool:
    """Return whether there is a direct flight from the iata_src airport to
    the iata_dst airport in the routes dictionary. iata_src may not
    be a key in the routes dictionary.

    >>> is_direct_flight('AA1', 'AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_direct_flight('AA2', 'AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    for key in routes:
        if key == iata_src and iata_dst in routes[key]:
            return True
    return False
            

    # Complete the function body

def is_valid_flight_sequence(iata_list: List[str], routes: RouteDict) -> bool:
    """Return whether there are flights from iata_list[i] to iata_list[i + 1]
    for all valid values of i. IATA entries may not appear anywhere in routes.

    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """

    # Complete the function body
    count = 0
    for i in range(len(iata_list)-1):
        for key in routes:
            if iata_list[i] == key\
               and iata_list[i + 1] in routes[key]:
                count += 1
    return count == len(iata_list) - 1

# Write the rest of the data analysis functions + your helper functions here

def count_outgoing_flights(iata: str, routes: RouteDict) -> int:
    """
    Return the number of outgoing flights for the airport 
    with the IATA code in the given route information.
    """
    return len(routes[iata])
    
def count_incoming_flights(iata: str, routes: RouteDict) -> int:
    """
    Return the number of incoming flights for the airport 
    with the IATA code in the given route information.
    """
    count = 0
    for key in routes:
        if iata in routes[key]:
            count += 1
    return count
    
def reachable_destinations(iata: str, n: int, routes: RouteDict) -> List[Set[str]]:
    """
    Return a list of the sets of IATA codes reachable from the first parameter 
    in steps from 0 up to (and including) the maximum number of hops
    """
    count = 0
    reachable = []
    while count <= n:
        count += 1
        reachable.append(routes[iata])
    return reachable

def get_score(routes: RouteDict) -> List[Tuple[int, str]]:
    """
    retrun a list of score (incoming and outgoing)
    """
    score_list = []
    for iata in routes:
        flights = count_outgoing_flights(iata, routes)\
            + count_incoming_flights(iata, routes) 
        airport = (flights, iata)
        score_list.append(airport)
    score_list.sort()
    return score_list

def find_max_and_pop(airport_list: List[Tuple[int, str]]) -> Tuple[str, int]:
    """
    get the max and remove the max in the list and get the second big one
    """
    max_num = max(airport_list)
    index = airport_list.index(max_num)
    airport = airport_list.pop(index)
    reverse_tuple = (airport[1], airport[0])
    return reverse_tuple

def sort_list(routes: RouteDict) -> List[Tuple[str, int]]:
    """
    make a list of the new airport list
    """
    sorted_list = [] 
    airport_score = get_score(routes) 
    i = 0
    while i < len(airport_score):
        sorted_list.append(find_max_and_pop(airport_score))
        i += 1
    return sorted_list

def find_busiest_airports(routes: RouteDict, limit: int) -> List[Tuple[str, int]]:
    """
    put all together
    precondition: limit > 0
    adding all the information above to make a list of airport
    """
    sorted_airport = sort_list(routes)
    if len(sorted_airport) <= limit:
        return sorted_airport
    else:
        while sorted_airport[limit - 1][1] == sorted_airport[limit][1]:
            limit -= 1
    return sorted_airport[:limit]
    
    
if __name__ == '__main__':
    """Uncommment the following as needed to run your doctests"""
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    #from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    #from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    #import doctest
    #doctest.testmod()
