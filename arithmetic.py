def add(num1, num2):
    """Returns the sum of int num1 and int num2"""

    return num1 + num2

#print "Result of 1 + 2 = {}".format(add(1,2))

def subtract(num1, num2):
    """Returns the int from subtracting int num2 from int num1"""

    return num1 - num2 

#print "Result of 3 - 2 = {}".format(subtract(3,2))


def multiply(num1, num2):
    """Returns the int product of multiplying int num1 and int num2"""

    return num1 * num2

#print "Result of 25 * 3 = {}".format(multiply(25,3))

def divide(num1, num2):

    """Returns the float result of dividing int num1 with int num2"""

    return float(num1) / float(num2) 

#print "Result of 18 / 5 = {}".format(divide(18,5))

def square(num1):
    """Returns the int result of squaring int num1"""
    
    return num1 * num1

#print "Square of 15 = {}".format(square(15))

def cube(num1):
    """Returns the cube of int num1"""

    return int(num1 * num1 * num1) 
 
#print "Cube of 3 = {}".format(cube(3))

def power(num1, num2):
    """Returns the result of raising int num1 to the power of int num2"""

    return int(num1 ** num2)

#print "Result of 4 to the power of 3 = {}".format(power(4,3))    

def mod(num1, num2):
    """Returns the remainder of int num1 divided by num2"""

    return int(num1 % num2)

#print "Remainder of 21 / 3 = {}".format(mod(21,3)) 

