import unittest

def El_COVID(age):
    result =""
    if age<0:
        result = "Invalid age"
    elif age<6:
        result  = "Not eligible"
    elif age<13:
        result = "Eligible for 1 dose"
    elif age<17:
        result = "Eligible for 2 doses"
    elif age<26:
        result = "Eligible for 3 doses"
    elif age<46:
        result = "Eligible for optional dose"
    elif age<61:
        result = "Must take optional dose"
    elif age<86:
        result = "See your GP for eligibility"
    elif age>85:
        result = "Invalid age"

    return result

class TestElCOVID(unittest.TestCase):

    def test_invalid_age_upper_boundary(self):
        self.assertEqual(El_COVID(-1), "Invalid age")

    def test_not_eligible_lower_boundary(self):
        self.assertEqual(El_COVID(0), "Not eligible")
        
    def test_not_eligible_upper_boundary(self):
        self.assertEqual(El_COVID(5), "Not eligible")
    
    def test_eligible_for_1_dose_lower_boundary(self):
        self.assertEqual(El_COVID(6), "Eligible for 1 dose")

    def test_eligible_for_1_dose_upper_boundary(self):
        self.assertEqual(El_COVID(12), "Eligible for 1 dose")

    def test_eligible_for_2_doses_lower_boundary(self):
        self.assertEqual(El_COVID(13), "Eligible for 2 doses")
        
    def test_eligible_for_2_doses_upper_boundary(self):
        self.assertEqual(El_COVID(16), "Eligible for 2 doses")
        
    def test_eligible_for_3_doses_lower_boundary(self):
        self.assertEqual(El_COVID(17), "Eligible for 3 doses")

    def test_eligible_for_3_doses_upper_boundary(self):
        self.assertEqual(El_COVID(25), "Eligible for 3 doses")
        
    def test_eligible_for_optional_dose_lower_boundary(self):
        self.assertEqual(El_COVID(26), "Eligible for optional dose")

    def test_eligible_for_optional_dose_upper_boundary(self):
        self.assertEqual(El_COVID(45), "Eligible for optional dose")

    def test_must_take_optional_dose_lower_boundary(self):
        self.assertEqual(El_COVID(46), "Must take optional dose")

    def test_must_take_optional_dose_upper_boundary(self):
        self.assertEqual(El_COVID(60), "Must take optional dose")

    def test_see_your_gp_for_eligibility_lower_boundary(self):
        self.assertEqual(El_COVID(61), "See your GP for eligibility")

    def test_see_your_gp_for_eligibility_upper_boundary(self):
        self.assertEqual(El_COVID(85), "See your GP for eligibility")

    def test_invalid_age_lower_boundary(self):
        self.assertEqual(El_COVID(86), "Invalid age")
        
if __name__ == '__main__':
    unittest.main()

