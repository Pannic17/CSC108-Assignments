from typing import Dict, List, Set, Tuple
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

if __name__ == '__main__':
    """Uncommment the following as needed to run your doctests"""
    from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    from flight_types_constants_and_test_data import TEST_ROUTES_SRC
    
    import doctest
    doctest.testmod()