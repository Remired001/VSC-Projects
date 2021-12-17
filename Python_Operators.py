x= 5
y= 9

py_operators= {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "division": "/"
}

print(type(py_operators))

def add(i, j):
    return i + j

def subtract(i, j):
    return i - j

def multiply(i, j):
    return i * j

def division(i, j):
    return i / j

result= multiply(x,y)

print(f"The result of {x} * {py_operators} {y} = {result}")