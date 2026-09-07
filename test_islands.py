import unittest
from count_islands import count_islands


class TestCountIslands(unittest.TestCase):

    def test_case_1_from_spec(self):
        grid = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
        ]
        self.assertEqual(count_islands(grid), 2)

    def test_case_2_diagonal_separation(self):
        grid = [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
        ]
        self.assertEqual(count_islands(grid), 3)

    def test_case_3_mixed_connectivity(self):
        grid = [
            [0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1],
        ]
        self.assertEqual(count_islands(grid), 2)

    def test_empty_and_single_cell(self):
        self.assertEqual(count_islands([]), 0)
        self.assertEqual(count_islands([[0]]), 0)
        self.assertEqual(count_islands([[1]]), 1)

    def test_all_land_and_all_water(self):
        all_water = [[0, 0], [0, 0]]
        all_land = [[1, 1], [1, 1]]
        self.assertEqual(count_islands(all_water), 0)
        self.assertEqual(count_islands(all_land), 1)

    def test_invalid_dimensions(self):
        ragged = [[0, 1], [1]]
        with self.assertRaises(ValueError):
            count_islands(ragged)

    def test_invalid_values(self):
        bad_grid = [[0, 2], [1, 0]]
        with self.assertRaises(ValueError):
            count_islands(bad_grid)


if __name__ == "__main__":
    unittest.main()
