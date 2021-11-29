import unittest
from flight_functions import is_valid_flight_sequence

# You can use this data in your tests if you want to
SMALL_ROUTES_DICT = {'AA1': {'AA2', 'AA3'}}
routes_dic =  {
    'AA1': {'AA2', 'AA4'},
    'AA2': {'AA3'},
    'AA3': {'AA4', 'AA1'},
    'AA4': {'AA1'}}

# You can (and should) also create and use other RouteDicts for your tests

class TestIsValidFlightSequence(unittest.TestCase):

    def test_valid_direct_flight(self):
        expected = True
        sequence = ['AA1', 'AA2']
        actual = is_valid_flight_sequence(sequence, SMALL_ROUTES_DICT)
        self.assertEqual(actual, expected)
        
    # Add tests below to create a complete set of tests without redundant tests
    # Redundant tests are tests that would only catch bugs that another test
    # would also catch.
    
    def is_valid_flight_sequence(self):
        expected1 = True
        expected2 = False
        sequence1 = ['AA3', 'AA1', 'AA2', 'AA1', 'AA2']
        sequence2 = ['AA3', 'AA1', 'AA2']
        sequence3 = []
        sequence4 = ['AA5','AA1']
        
        actual1 = is_valid_flight_sequence(sequence1, routes_dic)
        self.assertEqual(actual1, expected2)
        
        actual2 = is_valid_flight_sequence(sequence2, routes_dic)
        self.assertEqual(actual2, expected1)
        
        actual3 = is_valid_flight_sequence(sequence3, routes_dic)
        self.assertEqual(actual3, expected2)
        
        actual4 = is_valid_flight_sequence(sequence4, routes_dic)
        self.assertEqual(actual4, expected2)


if __name__ == '__main__':
    unittest.main(exit=False)
