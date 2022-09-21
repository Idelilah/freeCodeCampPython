import re

def formatter(numbers, solution=False):
    """Check the length of the array"""
    
    if len(numbers)>5:
        return "Error: Too many problems."

    for number in numbers:
        num=number.split(" ")
        operand=num[0]
        operator=num[1]
        operand2=num[2]

        if operator not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."

        if not operand.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand)>4 or len(operand2)>4:
            return "Error: Numbers cannot be more than four digits."

        arranged_numbers = ""
        if operator == "+":
            result = int(operand) + int(operand2)
            arranged_numbers=arranged_numbers+operand.rjust(2)+"/n "+operator+"/n "+operand2.rjust(2)+" /n"+"-"*4+"/n "+str(result).rjust(2)
 
            if solution:
                arranged_numbers = arranged_numbers + str(result).rjust(4)
        else:
            result = int(operand) - int(operand2)
            arranged_numbers=arranged_numbers+operand.rjust(2)+"/n "+operator+"/n "+operand2.rjust(2)+" /n"+"-"*4+"/n "+str(result).rjust(2)
 
            if solution:
                arranged_numbers = arranged_numbers + str(result).rjust(4)           