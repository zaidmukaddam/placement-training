"""
It is given that you can either take a car or a plane to travel between two cities.

• A car can only take you from city i to city i+1, i.e. two consecutive cities.
• a plane can take you from city i to any city j, where j>=i+2.

Find the number of ways to travel from city 0 to reach a city n. Since, the answer could be very large , return modulo 10^9+7

• Between any two consecutive cities, there are exactly a distinct working car
• Between any two cities that are not consecutive, there are exactly b distinct working planes.
• It is guaranteed that n is always a whole number.

n - no of cities to travel
a - no of cars working
b - no of planes working
"""

import unittest

def travel(n, a, b):
    # start writing your code here
    no_of_ways = 0
    if n == 1:
        no_of_ways = a
    elif n > 2:
        no_of_ways += b + b * a + a * b + a ** n
    elif n == 2:
        no_of_ways += a ** n + b
    return no_of_ways


class TestPractice(unittest.TestCase):
    def test_travel1(self):
        n, a, b = 3, 10, 20
        self.assertEqual(travel(n, a, b), 1420, 'Test 1 Failed')

    def test_travel2(self):
        n, a, b = 1, 99, 88
        self.assertEqual(travel(n, a, b), 99, 'Test 2 Failed')

    def test_travel3(self):
        n, a, b = 2, 10, 20
        self.assertEqual(travel(n, a, b), 120, 'Test 3 Failed')


if __name__ == '__main__':
    unittest.main()
