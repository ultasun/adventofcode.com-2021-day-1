#!/usr/bin/env python3

import unittest
from solution import count_increases_from_previous_values_in_sequence

class TestSolution(unittest.TestCase):
    def test_solution_test1(self):
        case = (199, 200, 208, 210, 200, 207, 240, 269, 260, 263)
        expected_result = 7
        result = count_increases_from_previous_values_in_sequence(case)
        self.assertEqual(result, expected_result)

    def test_solution_test2(self):
        case = [200, 199]
        expected_result = 0
        result = count_increases_from_previous_values_in_sequence(case)
        self.assertEqual(result, expected_result)

    def test_solution_test3(self):
        case = (199, 200)
        expected_result = 1
        result = count_increases_from_previous_values_in_sequence(case)
        self.assertEqual(result, expected_result)

    def test_solution_test4(self):
        case = (123, 'nonsense', 456)
        expected_result = None
        result = count_increases_from_previous_values_in_sequence(case)
        self.assertEqual(result, expected_result)       

if __name__ == '__main__':
    unittest.main()
