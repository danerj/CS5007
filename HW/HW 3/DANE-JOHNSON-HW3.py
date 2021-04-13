#   HW3 Assignment 
#   Author: <DANE> <JOHNSON> 
#   Save this file as DANE-JOHNSON-HW3.py



#   -------
#   Part 1:
#   -------

print("Part 1: Point")

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # x is intended to be a rational value.
    def setX(self, x):
        self.x = x
        
    # y is intended to be a rational value.
    def setY(self, y):
        self.y = y

    def toString(self):
        xstr = str(self.getX())
        ystr = str(self.getY())
        return "(" + xstr + ", " + ystr + ")"

    def equals(self, point):
        # Could also have used self.x, point.x, self.y, and point.y below.
        return (self.getX() == point.getX()) and (self.getY() == point.getY())

p1 = Point(0, 0)
p2 = Point(1, 2)

# Print out the coordinates of p1,p2 on the same line.
print(p1.toString() + ", " + p2.toString())

# Print out the result of calling equals on p1 with arg p2.
print(p1.equals(p2))

# Set the x-coordinate of p2 equal to the x-coordinate of p1.
# Set the y-coordinate of p2 equal to the y-coordinate of p1.
p2.setX(p1.getX())
p2.setY(p1.getY())

# Print out the result of calling equals on p1 with arg p2.
print(p1.equals(p2))

# Increment by 1 the x-coordinate of p2 using setX, getX.
p2.setX(p2.getX() + 1)

# Print out the result of calling equals on p1 with arg p2.
print(p1.equals(p2))

#   -------
#   Part 2:
#   -------

print("\n")
print("Part 2: Rectangle")

class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin  # bottom left corner of the rectangle.
        self.width = width
        self.height = height

    def perimeter(self):
        return 2*self.width + 2*self.height

    def area(self):
        return self.width * self.height

    def getOrigin(self):
        return self.origin

    def toString(self):
        string_rep = "{origin}, L={width}, H={height}.".format(
                origin = self.getOrigin().toString(),
                width = self.width,
                height = self.height
                )
        return string_rep

# Using the resulting forms of p1 and p2 after running Part 1!!!
r1 = Rectangle(p1, 2, 5.5)
r2 = Rectangle(p2, 3, 6)

# Print out the bottom left corner of r1 and the perimeter of r1.
print(r1.getOrigin().toString())
print(r1.perimeter())

# Print out the bottom left corner of r2 and the area of r2.
print(r2.getOrigin().toString())
print(r2.area())

# Print the string representations of r1 and r2 by calling their
# respective .toString() methods.
print(r1.toString())
print(r2.toString())

#   -------
#   Part 3:
#   -------

print("\n")
print("Part 3: Movable Rectangle")

class MovableRectangle(Rectangle):
    def __init__(self, origin, width, height):
        super().__init__(origin, width, height)
        self.move = False

    def unlock(self):
        self.move = True

    def lock(self):
        self.move = False

    def moveTo(self, new_origin):
        if self.move:
            self.origin = new_origin
        else:
            print("Warning: locked.")

    def toString(self):
        string_rep = "{origin}, W={width}, H={height}, Movable? {movable}".format(
                origin = self.getOrigin().toString(),
                width = self.width,
                height = self.height,
                movable = self.move
                )
        return string_rep

r3 = MovableRectangle(p1, 2, 2)

# Print the string representation of r3 using toString().
print(r3.toString())

# Create a point p3 of coordinates (5,15)
# Try to move the origin of p3 using moveTo().
# Print the string representation of r3 again.
p3 = Point(5,15)
r3.moveTo(p3)
print(r3.toString())

# Unlock r3 using unlock()
# Try to move the origin of p3 using moveTo().
# Print the string representation of r3 again.
r3.unlock()
r3.moveTo(p3)
print(r3.toString())

#   -------
#   Part 4:
#   -------

print("\n")
print("Part 4: Read File (Extra Credit?)")

import csv

class Tour:
    def __init__(self, filename):
        self.MyList = []
        with open(filename) as csvfile:
            for line in csvfile:
                self.MyList.append(line.strip("\n").split(";"))

# Below are various tests to confirm that the Tour class produces the expected results.
tour_files = ["tour17.csv", "tour26.csv", "tour40.csv", "tour48.csv", "tour58.csv"]

tour17 = Tour(tour_files[0])
print("The full list of stops in tour17 (printing tour17.MyList):\n" + str(tour17.MyList) + "\n")

print("Sampling first three and last three elements of MyList for each file:\n")
for tour_file in tour_files:
    tour = Tour(tour_file)
    print("The number of stops in " + tour_file + " is " + str(len(tour.MyList)))
    print("The first 3 stops of " + tour_file + " are " + str(tour.MyList[:3]))
    print("The last 3 stops of " + tour_file + " are " + str(tour.MyList[-3:]) + "\n")

