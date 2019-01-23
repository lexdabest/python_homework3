#function that accepts three variables
def checkNumbers(num1, num2, num3):
    if int(num1) == int(num2) or int(num2) == int(num3)  or int(num1) == int(num3):
        return True
    else:
        return False

theresult =checkNumbers(3,2,"1")
print(theresult)