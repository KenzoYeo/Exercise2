import unittest

def funmean(num1, num2, num3, num4):
    '''
    A function takes four integer inputs (num1, num2, num3, num4), and returns the mean four numbers
    if the numbers meet the basic requirement. The basic requirement is, if num1 is grater then num2
    and num3 is greater than or equal to num4, the result is mean of all number otherwise -1 is returned.  
    '''
    mean_result = -1
    if num1>num2 and num3>=num4:
        mean_result = (num1+num2+num3+num4)/4
    return mean_result

class TestFunMeanFunction(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(funmean(5, 3, 8, 4), 5.0)

    def test_invalid_input(self):
        self.assertEqual(funmean(3, 5, 8, 4), -1)
        self.assertEqual(funmean(5, 3, 4, 8), -1)

if __name__ == '__main__':
    unittest.main()
