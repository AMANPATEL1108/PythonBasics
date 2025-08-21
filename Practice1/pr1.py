
for i in range(5):
    print(i)

# ------------------------------------------------------------------------------------
count=1
while count<5:
    print("Count",count)
    count+=1

# ------------------------------------------------------------------------------------

def callMyName(name):
    print("hey are you"+name+"i am right")

# ------------------------------------------------------------------------------------
callMyName("aman")
def sum(a,b):
    return a+b

print(sum(5,10))

# ------------------------------------------------------------------------------------
name=input("Enter Your Name:")

print("Welcome"+name)
# ------------------------------------------------------------------------------------

a=int(input("Enter Number 1="))
b=int(input("Enter number 2="))
op=input("Enter oprator")


def calculator(a,b,op):
    if op=="+":
        print(a+b)
        return 
    elif op=="-":
        print(a-b)
        return
    elif op=="*":
        print(a*b)
        return 
    elif op=="/":
        print(a/b)
        return
    else:
        print("Print Correct oprator")

print(calculator(a,b,op))
# ------------------------------------------------------------------------------------

colors=["black","blue","yellow"]
print(colors)
for i in colors:
    print(i)

# ------------------------------------------------------------------------------------

points=(3,4)
print(points)
for i in points:
    print(i)
# ------------------------------------------------------------------------------------

person = {"name": "Alice", "age": 30}

for key, value in person.items():
    print(key, ":", value)

# ------------------------------------------------------------------------------------

persons = [{"name": "Alice", "age": 30},{"name": "Aman", "age": 25}]

for person in persons:
    for key, value in person.items():
        print(person)
        print(key, ":", value ,"")

# ------------------------------------------------------------------------------------

try:
    result=10/0
except ZeroDivisionError:
        print("You can't divide by zero!")

# ------------------------------------------------------------------------------------
import math
import random
print(math.sqrt(16))

print(random.randint(1, 10))
# ------------------------------------------------------------------------------------
with open("sample.txt", "w") as f:
        f.write("Hello, file!")

with open("sample.txt", "r") as f:
        content = f.read()
        print(content)
# ------------------------------------------------------------------------------------
class Person:
        def __init__(self, name):
             self.name = name
        
        def greet(self):
                        print("Hello, I am " + self.name)

p = Person("Aman")
p.greet()


