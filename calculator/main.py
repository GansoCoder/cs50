# First "scren" shown
print("Calculator 0.0.1\n")
print("1. Sum")
print("2. Multiply")
print("3. Div")
print("4. Sub")

# IF the user writes a number that is not 1,2,3 or 4 it asks again.
type = input("f: ")
if int(type) != 1 or int(type) != 2 or int(type) != 3 or int(type) != 4:
    type = input("f: ")

x = input("What's the value of x: ")
y = input("What's the value of y: ")

# functions of the math
def sum(x, y):
    ans = x + y
    return ans

def mul(x, y):
    ans = x * y
    return ans

def div(x, y):
    ans = x / y
    return ans

def sub(x, y):
    ans = x - y
    return ans

# selects the math used
if int(type) == 1:
    sum(x, y)
    print(ans)
    
elif int(type) == 2:
    mul(x, y)
    print(ans)

elif div(x, y) == 3:
    div(x, y)
    print(ans)

elif sub(x, y) == 4:
    sub(x, y)
    print(ans)