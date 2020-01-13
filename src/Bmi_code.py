class Bmi_code:

    @staticmethod
    def bmi_calc(weight, height):
        if type(weight) != int and type(weight) != float:
            return "Worng Type"
        if height <= 0 :
            return "Invalid height"
        if weight <= 0:
            return "Invalid weight"
        return weight / pow(height,2)

    @staticmethod
    def bmi_check(bmi):
        if type(bmi) != int and type(bmi) != float:
            return "Worng Type"
        if(bmi > 18.5 and bmi < 25):
            return "A proper bmi"
        elif (bmi > 25):
            return "Overweight"
        elif (bmi > 0 and bmi < 18):
            return "Underweight"
        elif (bmi < 0):
            return "Invalid_Bmi"