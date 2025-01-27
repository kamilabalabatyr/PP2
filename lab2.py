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

#10
