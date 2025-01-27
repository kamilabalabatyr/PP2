print(10 > 9)
print(10 == 9)
print(10 < 9)

#1
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#2  
print(bool("Hello"))
print(bool(15))

#3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#4
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#5
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#6
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#7
def myFunction() :
  return True

print(myFunction())

#8
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#9
x = 200
print(isinstance(x, int))

#LISTS
#1
thislist = ["apple", "banana", "cherry"]
print(thislist)


#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#5
list1 = ["abc", 34, True, 40, "male"]

#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

