import unittest
from actividad_10 import Tetromino

class TestTetromino(unittest.TestCase):
    def setUp(self):
        self.T = Tetromino([
            ['.', '.', '.'],
            ['.', '@', '@'],
            ['@', '@', '.']
        ])
        self.Z1 = Tetromino([
            ['.', '.', '.'],
            ['@', '@', '.'],
            ['.', '@', '@']
        ])
        self.Z2 = Tetromino([
            ['.', '.', '@'],
            ['.', '@', '@'],
            ['@', '@', '.']
        ])

    def test_rotate(self):
        rotated_T = self.T.rotar()
        expected_result = Tetromino([
            ['@', '.', '.'],
            ['@', '@', '.'],
            ['.', '@', '.']
        ])
        self.assertEqual(str(self.T), str(expected_result))

    def test_equals(self):
        self.assertTrue(self.Z1.iguales(self.Z2))

    def test_similar(self):
        self.assertTrue(self.Z1.similares(self.Z2))

if __name__ == '__main__':
    unittest.main()
