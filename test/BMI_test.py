import unittest
from src.Bmi_code import Bmi_code

class MyTestCase(unittest.TestCase):
    def test_Zero_dividing(self):

        #sub_values
        weight_1 = 0
        weight_2 = 0
        weight_3 = 3

        height_1 = 0
        height_2 = 3
        height_3 = 1

        #assume
        expected1 = "Invalid height"
        expected2 = "Invalid weight"
        expected3 = 3


        #action
        result1 = Bmi_test.bmi_calc(weight_1, height_1)
        result2 = Bmi_test.bmi_calc(weight_2, height_2)
        result3 = Bmi_test.bmi_calc(weight_3, height_3)


        #expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


    def test_Check_type(self):

        #sub_values
        weight_1 = 'a'
        weight_2 = 'b'
        weight_3 = 3

        height_1 = 'b'
        height_2 = 'b'
        height_3 = 1

        #assume
        expected1 = "Worng Type"
        expected2 = "Worng Type"
        expected3 = 3


        #action
        result1 = Bmi_test.bmi_calc(weight_1, height_1)
        result2 = Bmi_test.bmi_calc(weight_2, height_2)
        result3 = Bmi_test.bmi_calc(weight_3, height_3)


        #expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


    def test_Bmi_Check(self):

        #sub_values
        bmi_1 = 17
        bmi_2 = 22.5
        bmi_3 = 27
        bmi_4 = "a"
        bmi_5 = -10

        #assume
        expected1 = "Underweight"
        expected2 = "A proper bmi"
        expected3 = "Overweight"
        expected4 = "Worng Type"
        expected5 = "Invalid_Bmi"


        #action
        result1 = Bmi_test.bmi_check(bmi_1)
        result2 = Bmi_test.bmi_check(bmi_2)
        result3 = Bmi_test.bmi_check(bmi_3)
        result4 = Bmi_test.bmi_check(bmi_4)
        result5 = Bmi_test.bmi_check(bmi_5)


        #expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)

if __name__ == '__main__':
    unittest.main()
