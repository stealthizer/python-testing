from unittest import TestCase
from basic_operations import basic_operations

class TestOperations(TestCase):
    def setUp(self):
        self.basicOps = basic_operations()

    def test_sum(self):
        basicSum = self.basicOps.basic_sum(5, 6)
        self.assertEqual(basicSum, 11)
    
    def test_subb(self):
        basicSubb = self.basicOps.basic_subb(5, 6)
        self.assertEqual(basicSubb, -1)

    def test_multiplication(self):
        basicMultiplication = self.basicOps.basic_multiplication(5, 6)
        self.assertEqual(basicMultiplication, 30)
    
    def test_division(self):
        basicDivision = self.basicOps.basic_division(8, 2)
        self.assertEqual(basicDivision, 4)

    def test_division_should_avoid_infinite(self):
        basicDivision = self.basicOps.basic_division(8, 0)
        self.assertEqual(basicDivision, "division by zero")
