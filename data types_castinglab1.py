#Getting the Data Type
x = 5
print(type(x))

#Python Numbers
#1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#2
print(type(x))
print(type(y))
print(type(z))

#3
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#4
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#5
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#6
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#7
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#8
import random

print(random.randrange(1, 10))

#Python Casting

#1
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0

#3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

