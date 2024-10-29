import unittest
from src.math_quiz import get_random_integer, get_random_operator, perform_operation

class TestMathGame(unittest.TestCase):

    def test_function_get_random_integer(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(10):
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_get_random_operator(self):
        """Test if the operator returned is one of the allowed operators ('+', '-', '*')."""
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):
            operator = get_random_operator()
            self.assertIn(operator, valid_operators)

    def test_function_perform_operation(self):
        """Test if the operation is performed correctly with various test cases."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 0, '*', '10 * 0', 0),
            (0, 0, '+', '0 + 0', 0)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
