#   HW2 Assignment 
#   Author: <DANE> <JOHNSON> 
#   Save this file as DANE-JOHNSON-HW2.py



#   -------
#   Part 1:
#   -------

print("Part 1: Patterns")

#   Part 1.1 (Rectangle)

#   Given nonnegative integers n,m prints out
#   two identical rectangles of width n and height m,
#   separated by an empty column, using the symbol ’∗’.
#   Implementation using for loops instead of recursion.

def rectangle(n,m):

    stars = ''

    #   Create the string for the 'width' of a rectangle.
    for i in range(n):

        stars += '*'

    #   Create two rectangle 'widths' separated by column.
    stars = stars + ' ' + stars

    #   Print out m rows of the string created above.
    for i in range(m):

        print(stars)

print('Calling rectangle(4,6) produces: \n')
rectangle(4,6)

#   Part 1.2 (Triangle)

def triangle(n):

    spaces_count = n-1
    stars = ''
    
    for counter in range(n):
        
        space = ''
        
        for i in range(spaces_count):
            
            space += ' '
            
        if counter == 0:

            stars += '*'
            print(space + stars + space)

        else:

            stars = '*' + stars + '*'
            print(space + stars + space)

        spaces_count -= 1
        
print('Calling triangle(6) produces: \n')
triangle(6)



#   -------
#   Part 2:
#   -------

print('\n')
print("Part 2: Functions on Lists")

# Given a list, clean1 returns a new list with only one occurence
# of each integer in the original list (which is not modified).
def clean1(aList):

    tmp = []

    # Add elements to tmp if they are not already contained in tmp
    for element in aList:

        if element not in tmp:

            tmp.append(element)

    # The new list without duplicates is 'tmp'
    return tmp

al = [1,2,3,4,4,4,5,1,2,1,5]
newlist = clean1(al)
print(al)
print(newlist)



#   -------
#   Part 3:
#   -------

print('\n')
print("Part 3: Functions on Lists")

# clean2 removes duplicate occurences of an integer in a list.
# The function modifies its input instead of returning a list
# with all duplicates removed. This problem is easier to solve
# if you are allowed to use .sort() on the list but it is unclear
# whether this is ok so I avoid using this command.
def clean2(aList):

    # Start inspection by looking at the end of the list.
    index = len(aList) - 1

    # The loop ends on the second element of the list since
    # at index = 0 there can be no duplicates preceding aList[0].
    while index > 0:
        
        # Inspect elements preceding the current element and
        # remove the first occurence of any duplicate.
        while aList[index] in aList[:index]:

            aList.remove(aList[index])
            # By removing an element the list length decreases
            # and so to continue working with the current element,
            # need to decrement by one.
            index -= 1
            
        # Decrement once more after removing all duplicates.
        index -=1

al = [1,2,3,4,4,4,5,1,2,1,5]
print(al)
clean2(al)
print(al)

##  More tests

##bl = [1,1,1,1,1,1]
##print(bl)
##clean2(bl)
##print(bl)

##
##cl = []
##clean2(cl)
##print(cl)
##
##dl = [3,3,3,-4,0,5,6,5,6,5,6,5,6, 'hello']
##clean2(dl)
##print(dl)



#   -------
#   Part 4:
#   -------

print('\n')
print("Part 4: Functions on Lists")

# The function fct determines which elements in a list are powers of
# 2 and creates a string listing all of these elements. The function
# relies on the fact that an integer is a power of 2 if and only if
# repeated division by 2 terminates with a result of 1.
def fct(aList):

    powers_of_two = ''

    for element in aList:

        # All powers of 2 are positive. This avoids unecessary
        # division for negative elements and avoids an infinite
        # loop in the case that element == 0. 
        if element > 0:
            
            
            dividend = element
            
            # Repeatedly divide by two until the remainder
            # is nonzero (process terminates eventually for
            # divident != 0).
            while dividend % 2 == 0:

                dividend = dividend / 2

            # If an integer is a power of 2, repeatedly dividing by
            # 2 terminates with the result being 1.
            if dividend == 1:

                powers_of_two = powers_of_two + str(element) + ','

    return powers_of_two[:len(powers_of_two)-1]

print('Calling print on fct on [1, 2, 3, 4, 5, 16, 255, 256, −1, −2, 84] produces:')
al = [1,2,3,4,5,16,255,256,-1,-2,84]
print(fct(al))

## More Tests
##bl = [0,4096,-2,17, -0,6, 32]
##print(fct(bl))



#   -------
#   Part 5:
#   -------

print('\n')
print("Part 5: Taylor Series")

import math

# The function taylor calculates the Taylor Polynomial of Order n
# for the mathematical function f(x) = sin(x).
def taylor(x,n):

    sum = 0

    # Adding terms corresponding to orders 1 through n.
    for k in range(1,n+1):

        sum = sum + (-1)**(k+1)*x**(2*k-1) / math.factorial(2*k-1)

    return sum

x = math.pi/2
print(math.sin(x))
print(taylor(x,7))

##x = math.pi/4
##print(math.sin(x))
##print(taylor(x,5))



#   -------
#   Part 6:
#   -------



print('\n')
print("Part 6: Extra Credit???")


#  The function consecutives(aList) takes a list of integers as
#  argument and returns the maximum number of consecutive integers
#  that are all equal within this list. 
def consecutives(aList):

    # If a list contains no numbers, there can be no consecutives.
    if len(aList) == 0:
        return 0

    index = 0
    consecutive_count = 1
    max_consecutive_count = 1

    while index < len(aList)-1:

        # If the current value matches the next value,
        # increase tally of consecutive occurences for
        # this value.
        if aList[index] == aList[index+1]:

            consecutive_count += 1

        # If value doesn't match next value, decide whether
        # this current tally is the largest tally so far.
        else:

            max_consecutive_count = max(consecutive_count,max_consecutive_count)
            consecutive_count = 1

        index += 1
        # A final check at the end of the list if the largest tally
        # occurs from the rightmost elements of the list.
        max_consecutive_count = max(consecutive_count,max_consecutive_count)

    return max_consecutive_count

l1 = [1,1,1,3,3,4,4,4,4,4,3,1,7,3,3,4,4]
l2 = []
l3 = [1,2,1,1,2,1,1]
print(consecutives(l1)) # Should get 5
print(consecutives(l2)) # Should get 0
print(consecutives(l3)) # Should get 2

## Extra Tests
##a = [1,1,1,3,3,4,4,4,4,4,6]
##b = [1,1,1,3,3,4,4,4,4,4]
##c = [3,3,3,3,3,3,1,2,3,4,5,6,7]
##d = [-1,1,-2,2,0,0,0,-3,3,4,4]
##print(consecutives(a)) # Should get 5
##print(consecutives(b)) # Should get 5
##print(consecutives(c)) # Should get 6
##print(consecutives(d)) # Should get 3



