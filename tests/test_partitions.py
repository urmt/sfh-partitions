import unittest
from partitions import partition_exact, partition_asymptotic, is_forbidden_configuration

class TestPartitions(unittest.TestCase):

    def test_small_exact(self):
        self.assertEqual(partition_exact(0), 1)
        self.assertEqual(partition_exact(1), 1)
        self.assertEqual(partition_exact(4), 5)  # known value

    def test_asymptotic(self):
        # asymptotic should be close for large n
        exact = partition_exact(50)
        approx = partition_asymptotic(50)
        self.assertTrue(abs(exact - approx) / exact < 0.05)

    def test_forbidden(self):
        self.assertTrue(is_forbidden_configuration(4))   # 5*0+4
        self.assertTrue(is_forbidden_configuration(5))   # 7*0+5
        self.assertTrue(is_forbidden_configuration(6))   # 11*0+6
        self.assertFalse(is_forbidden_configuration(8))

if __name__ == "__main__":
    unittest.main()
