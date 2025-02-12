import unittest
from temperature_sensor import process_temperatures


class TestTemperatureSensor(unittest.TestCase):
    # Test 1 check the minimum boundry
    def test_minimum_boundry(self):
        """check the minimum boundry for process_temperature"""
        output = "Min: -50°C, Max: -50°C, Avg: -50°C"
        self.assertEqual(process_temperatures([-50]),output)
    
    # Test 2 check the maximum boundry
    def test_maximum_boundry(self):
        """check the maximum boundry for process_temperature"""
        output = "Min: 150°C, Max: 150°C, Avg: 150°C"
        self.assertEqual(process_temperatures([150]),output)

    # Test 3 check the near low and top boundry
    def test_near_boundry(self):
        """check the near low and top boundry"""
        output = "Min: -49°C, Max: 149°C, Avg: 50°C"
        self.assertEqual(process_temperatures([-49,149]),output)
    
    # Test 4 check mixed valid and invalid inputs
    def test_mixed_input(self):
        """check mixed valid and invalid inputs"""
        output = "Out-of-bound value detected"
        self.assertEqual(process_temperatures([-60,20,160]),output)

    # Test 5 check alphabetic characters in input
    def test_alphabetic_input(self):
        """check alphabetic characters in input"""
        output = "Invalid input detected"
        self.assertEqual(process_temperatures([20,"abc",30]),output)
    
    # Test 6 check special characters in input
    def test_special_input(self):
        """check special characters in input"""
        output = "Invalid input detected"
        self.assertEqual(process_temperatures([10,"@",-40]),output)

    # Test 7 check large input values
    def test_large_input(self):
        """Check large input"""
        output = "Out-of-bound value detected"
        self.assertEqual(process_temperatures([2**31-1,-2**31]),output)

    # Test 8 check all inputs are the same
    def test_same_input(self):
        """checks all inputs are same"""
        output = "Min: 50°C, Max: 50°C, Avg: 50°C"
        self.assertEqual(process_temperatures([50,50,50]),output)
    
    # Test 9 check empty input
    def test_empty_input(self):
        """checks empty input"""
        output = "No input provided."
        self.assertEqual(process_temperatures([]),output)

