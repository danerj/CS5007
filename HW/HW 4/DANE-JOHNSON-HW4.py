#   HW4 Assignment 
#   Author: <DANE> <JOHNSON> 
#   Save this file as DANE-JOHNSON-HW4.py


#   -------
#   Part 0:
#   -------

from matplotlib import pyplot as plt
import numpy as np

#   -------
#   Part 1:
#   -------

print("Part 1: Archimedean Spiral")

def arc():
    #need to add 0.01 in the second arg to include 5pi
    t = np.arange(0,5*np.pi + 0.01, 0.01)
    x = t * np.cos(t)
    y = t * np.sin(t)
    plt.plot(x, y, color='green')
    plt.title("Archimedean Spiral for $t \in [0,5 \pi ]$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

arc()
plt.close("all")

#   -------
#   Part 2:
#   -------

print("\n")
print("Part 2: Heart")

def heart():
    #need to add 0.01 in the second arg to include 2pi
    t = np.arange(0,2*np.pi + 0.01, 0.01)
    x = 16*(np.sin(t))**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2.5*np.cos(3*t) - np.cos(4*t)
    plt.plot(x, y, color = "red", linestyle = "--")
    plt.title("Heart for $t \in [0,2 \pi ]$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

plt.close("all")
heart()

#   -------
#   Part 3:
#   -------

print("\n")
print("Part 3: Graphs")

# 1) We can visualize this problem by letting nodes represent
# the products P_1, ... , P_k and letting the edges connect
# products that are allowed to be shipped together. For example,
# there would be edges connecting the node that represents P_1
# to the nodes that represent products P_3, ... , P_(k-1) but
# there would be no edges connecting the nodes representing P_2
# and P_k to the the node for P_1 since neither of P_2 and P_k
# are allowed to be shipped with P_1.

# 2) The algorithm should return 2 if k is even and 3 is odd
# While it would be simple to just make this the algorithm,
# that may not be allowed. So my approach is to start with
# item P_1 and then since P_1 is loaded, move on the next
# allowable item, P_3, and so on. Then when all allowable
# products are loaded, move on to P_2 and all remaining allowable
# products. Repeat until all products are shipped. This does
# not enumerate all possibilities in order to find the result. 

def minimum_shipments(k):
    if k < 2 or not isinstance(k, int):
        print("k must be an integer greater than 1")
        return
    
    loaded_inventory = [False for i in range(k)]
    shipments = 0
    for p in range(len(loaded_inventory)):
        if not loaded_inventory[p]:
            shipments += 1
            loaded_inventory[p] = True
            load_next = (p + 2) % k
            while not loaded_inventory[load_next] and load_next % (k-1) != p:
                loaded_inventory[load_next] = True 
                load_next = (load_next+2) % k

    return shipments

# Tests
##print(minimum_shipments(1))
##print(minimum_shipments(2))
##print(minimum_shipments(3))
##print(minimum_shipments(4))
##print(minimum_shipments(5))
##print(minimum_shipments(6))
##print(minimum_shipments(7))
##print(minimum_shipments(8))
##print(minimum_shipments(9))
##print(minimum_shipments(10))
##print(minimum_shipments(9999))
##print(minimum_shipments(3578))

#   -------
#   Part 4:
#   -------

print("\n")
print("Part 4: Algorithm")

def egyptian(x,y):
    if not isinstance(x, int) or not isinstance(y,int):
        print("Inputs must be integers")
        return
    if x <= 2 or y <= 2:
        return x*y
    if y % 2 == 0:
        return 2*egyptian(x, y//2)
    return x+egyptian(x, y-1)

# Tests
##print(egyptian(7,5))
##print(egyptian(1,1))
##print(egyptian(2,1))
##print(egyptian(10, 0))
##print(egyptian(8,14))
##print(egyptian(9,6))
##print(egyptian(4, 3.5))
##print(egyptian(4, 3.0))

