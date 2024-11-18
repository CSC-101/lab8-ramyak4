import unittest

from group import groups_of_3


class TestCases(unittest.TestCase):

    def test_groups_of_3(self):
        input = [1,2,3,4,5,6,7,8,9]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(expected, groups_of_3(input))
    def test_groups_of_3_2(self):
        input = [1,2,3,4,5,6,7,8]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        self.assertEqual(expected, groups_of_3(input))
if __name__ == '__main__':
    unittest.main()

