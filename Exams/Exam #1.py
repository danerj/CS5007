INTRODUCTION TO PROGRAMMING CONCEPTS, DATA STRUCTURES 
Exam #1
May 8, 2019




----------------------------------------------
Part 1: Multiple Choice (30 Marks)
----------------------------------------------


1. Each pass through a loop is called a/an_ _ _ _ _ _ _ _ _ _ _ _ _ _
a) Enumeration
b) Iteration
c) Permutation
d) Combination


The correct answer is []






2. Recursion is a programing technique in which the solution of a problem is achieved by solving_ _ _ _ _ _ _ _ _ _ _ _ _ _
a) Larger instances of different problems
b) Larger instances of the same problem
c) Smaller instances of the same problem
d) Smaller instances of different problems


The correct answer is []






3. In recursion, the condition for which the recursive function will stop calling itself is known as_ _ _ _ _ _ _ _ _ _ _ _ _ _
a) Best case
b) Worst case
c) Base case
d) First case


The correct answer is []






4. What happens if the base condition isn’t defined in a recursive function?
a) Program gets into an infinite loop
b) Program runs once
c) Program runs n number of times where n is the argument given to the function
d) The function still runs correctly


The correct answer is []






5. Which of the following statements is true?
a) Recursion is always better than iteration
b) Iteration is always better than recursion
c) Recursion uses more memory compared to iteration
d) Recursion uses less memory compared to iteration


The correct answer is []






6. Each time a function is invoked, the system stores parameters and local variables in an area of memory, known as_ _ _ _ _ _ _ _ _ _ _ _ _ _, which stores elements in last-in first-out fashion.
 a) Heap
 b) Storage area
 c) Stack
 d) Array


The correct answer is []






7. What do while-loops do?
a) Repeat a piece of code a given number of times
b) Repeat a piece of code until a condition is true
c) Repeat a piece of code until a condition is false
d) Repeat a piece of code indefinitely


The correct answer is []






8. A Python line comment begins with_ _ _ _ _ _ _ _ _ _ _ _ _ _
a) //
b) /*
c) #
d) $$


The correct answer is []






9. In Python, a function_ _ _ _ _ _ _ _ _ _ _ _ _ _
a) Must have at least one parameter
b) May have no parameters
c) Must always have a return statement
d) Must always have a print statement


The correct answer is []






10. The output of the line of code shown below is:_ _ _ _ _ _ _ _ _ _ _ _ _ _
not(10<20) and not(10>30)
a) True
b) False
c) Error
d) None


The correct answer is []






-------------------------------------------
Part 2: Code Review (20 Marks)
-------------------------------------------


Is there anything wrong with the following code? If yes, what is the problem? If no, why?




>>> def fun(s):
        print (s[0])
        if len(s) == 0:
                return
        fun (s[1:len(s)])


######## ADD YOUR ANSWER HERE ########






-------------------------------------------------
Part 3: Iterative Function (25 Marks)
-------------------------------------------------


Given a list L1, write a Python function func1 that returns the reverse of L1 as follows


>>> L1 = [1,2,3,4,5,6]
>>> L2 = func1(L1)
>>> print (L2)
[6, 5, 4, 3, 2, 1]




Note that func1 must be coded as an *iterative function*.


######## ADD YOUR CODE OF FUNC1 HERE ########






---------------------------------------------------
Part 4: Recursive Function (25 Marks)
---------------------------------------------------


Given a list L1, write a Python function func2 that returns the reverse of L1 as follows


>>> L1 = [1,2,3,4,5,6]
>>> L2 = func2(L1)
>>> print (L2)
[6, 5, 4, 3, 2, 1]


Note that func2 must be coded as a *recursive function*.


######## ADD YOUR CODE OF FUNC2 HERE ########






