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


#ACCESS LIST ITEMS
#1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
  
#CHANGE VALUE 
#1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#ADD LIST ITEMS
#1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#REMOVE LIST ITEMS
#1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#6
thislist = ["apple", "banana", "cherry"]
del thislist

#7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#LOOP THROUGH LIST
#1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
#2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#LIST COMPREHENSION
#1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#3
newlist = [x for x in fruits if x != "apple"]

#4
newlist = [x for x in fruits]

#5
newlist = [x for x in range(10)]

#6
newlist = [x for x in range(10) if x < 5]

#7
newlist = [x.upper() for x in fruits]


#8
newlist = ['hello' for x in fruits]

#9
newlist = [x if x != "banana" else "orange" for x in fruits]




  