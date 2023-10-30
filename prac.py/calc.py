def add(x, y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y ==0:
        raise ValueError('Cannot divide by Zero')
    return x/y

print(add(10,20))
print(sub(30,20))
print(mul(10,20))
print(div(10,20))