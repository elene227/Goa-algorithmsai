def convert_number(number, from_base, to_base):

    decimal_number = int(number, from_base)


    if to_base == 10:
        return decimal_number
    

    result = ""
    while decimal_number > 0:
        result = str(decimal_number % to_base) 
        decimal_number = decimal_number // to_base

    return result
                                                                # ათწლიანში გადაყვანა
number = input("რიცხვი: ")
from_base = int(input("საწყისი ბაზა: "))
to_base = int(input("მიზნობრიივ ბაზა: ")) # გადაქცევა რიცხვის რა ბაზაშიც გვინდა 

convert_number = (number, from_base, to_base)

print (convert_number)