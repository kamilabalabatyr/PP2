#SETS
#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


#4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#7
set1 = {"abc", 34, True, 40, "male"}

#8
myset = {"apple", "banana", "cherry"}
print(type(myset))

#9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#Access Set Items
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#2
thisset = {"apple", "banana", "cherry"}


#3
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#Add Set Items
#1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Set Items
#1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Loop Sets
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#Join Sets
#1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


#3
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#5
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


#6
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#7
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#8
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#9
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#10
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#11
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#12
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#13
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


#14
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#15
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#16
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

