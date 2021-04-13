#   HW1 Assignment 
#   Author: <INSERT FIRST NAME> <INSERT LAST NAME> 
#   Save this file as FIRSTNAME-LASTNAME-HW1.py



#   -------
#   Part 1:
#   -------

print("Part 1")

#   Let the following variables be defined with the following
#   values

a = 5.0
b = 2.5
c = 9.0

import math

#   1a: (write expression in place of the zero in the next line)
expr_1a = 4*a*b + b*c
print("The value of expression 1a is", expr_1a)

#   1b: (write expression in place of the zero in the next line)
expr_1b = b**3
print("The value of expression 1b is", expr_1b)

#   1c: (write expression in place of the zero in the next line)
expr_1c = (a*b)**.5
#   Could also import math and calculate expr_1c = math.sqrt(a*b)
print("The value of expression 1c is", expr_1c)

#   1d: (write expression in place of the zero in the next line)
expr_1d = (a*c + b*a) / (b*c)
print("The value of expression 1d is", expr_1d)

#   1e: (write expression in place of the zero in the next line)
expr_1e = a**2 - b**4 + 2*a*b
print("The value of expression 1e is", expr_1e, "\n")

#   -------
#   Part 2:
#   -------

print("Part 2")

#   2a: (write expression in place of the zero in the next line)
expr_2a = (8//6)*6 
print("The value of expression 2a is", expr_2a)

#   2b: (write expression in place of the zero in the next line)
expr_2b = (8/6)*6
print("The value of expression 2b is", expr_2b)

#   Write here your comment (max. two sentences)
#
#   Using the '//' operator produces the quotient of integer
#   division of 8 by 6 (which is 1 since 6 goes into 8 only 1
#   time) while the '/' is normal (floating point) division.
#   So (8//6)*6 = 1*6 = 6 and (8/6)*6 = 8
#



#   -------
#   Part 3:
#   -------

print("\nPart 3")

#   Let the following variables be defined with the following
#   values

a = True
b = False
c = False

#   3a: (write expression in place of the True in the next line)
expr_3a = a and (b or c)
print("The value of expression 3a is", expr_3a)

#   3b: (write expression in place of the True in the next line)
expr_3b = (not a) or (b or c)
print("The value of expression 3b is", expr_3b)

#   3c: (write expression in place of the True in the next line)
expr_3c = (a and b) or (not c)
print("The value of expression 3c is", expr_3c)

#   3d: (write expression in place of the True in the next line)
expr_3d = (not a) or ((not b) or (not c))
print("The value of expression 3d is", expr_3d)

#   -------
#   Part 4:
#   -------

print("\nPart 4")

#   1) Write here your windChill function.


def WindChill(T,V):
    wind_chill = 13.13 + 0.621 * T - 12.1 * V**0.15 + .3967 * T * V**0.16
    print("At", T, "C and", 30, "kph winds, it feels like", wind_chill, "C")






#   Call here your windChill function with arguments -20 for T and 30 for V. 

T = -20
V = 30
WindChill(T,V)



#   2) Write here your windChill2 function.

def WindChill2(T,V):
    wind_chill = 13.13 + 0.621 * T - 12.1 * V**0.15 + .3967 * T * V**0.16
    return wind_chill
    





#   Call here your windChill2 function with arguments -20 for T and 30 for V.
#   Print the result of this call.

wind_chill = WindChill2(T, V)
print("At", T, "C and", 30, "kph winds, it feels like", wind_chill, "C")








#   -------
#   Part 5:
#   -------

print("\nPart 5")


#   List here the 5 errors in the Python function euc
#
#   1. There is a duplicate 'y1' in the function argument. Should be 'y2'.
#   2. The function tries to assign 'lambda' as a variable but lambda is
#      is an expression used for lambda functions so we need a different variable name.
#   3. The exponent uses integer division '1//2' but we need regular division '1/2'.
#   4. The 'return' statement must be indented.
#   5. The print statement tries to print the string 'result' instead of
#      the numerical value of 'result' calculated using the function.
#


#   Write correcly the function, the call of this function and
#   the print statement:



def euc(x1,y1,x2,y2):
    alpha = (x1-x2)**2
    gamma = (y1-y2)**2
    return((alpha+gamma)**(1/2))
result = euc(1,3,2,7)
print(result)


#   ------------
#   Extra credit
#   ------------

print("\nExtra credit")

def myFct(value):
    if(value==1):
        return value
    else:
        return value+myFct(value-1)


print(myFct(3))
print(myFct(4))
print(myFct(5))
#print(myFct(-3))
#print(myFct(0))

#   Write here your comment:
#
#   The function 'myFct' calculates the sum of the positive integers
#   less than or equal to the input 'value'. Note that using negative,
#   zero, or non-integer inputs for 'value' produces an error.

#   Write here a simpler function, doing the same without
#   if/else statements and without re-calling myFct

def myFct(value):
    # Write here the code of the function in place of the print('TODO')
    summation = (value * (value + 1)) // 2
    return summation

print(myFct(3))
print(myFct(4))
print(myFct(5))

# END
