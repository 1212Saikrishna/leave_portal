import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        # result = calc.add(10,20)
        self.assertEqual(calc.add(10,20), 30)
    def test_sub(self):
        # result = calc.add(10,20)
        self.assertEqual(calc.sub(10,20), -10)
    def test_mul(self):
        # result = calc.add(10,20)
        self.assertEqual(calc.mul(10,20), 200)
    def test_div(self):
        # result = calc.add(10,20)
        self.assertEqual(calc.div(10,20), 0.5)
        with self.assertRaises(ValueError):
            calc.div(10,0)

if __name__ == '__main__':
    unittest.main()
    