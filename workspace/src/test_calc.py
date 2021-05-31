import unittest
import calc

class TestCalc(unittest.TestCase):
    
    
    def setUp(self):
        """Set up test case input before each unit test"""
        self.numPairA = 10,5
        self.sumPairB = 10,0
        
    def tearDown(self):
        """Run below to do any clean up after each unit test"""
        result = 0
    
    
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = calc.subtract(10,5)
        self.assertEqual(result, 5)
        
    def test_muliply(self):
        result = calc.multiply(10,5)
        self.assertEqual(result, 50)
        
    def test_divide(self):
        result = calc.divide(10,5)
        self.assertEqual(result, 2)
       
#         self.assertRaises(ZeroDivisionError, calc.divide, 10, 0)

        # alternative nicer way
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10,0)

if __name__ == "__main__":
    unittest.main()