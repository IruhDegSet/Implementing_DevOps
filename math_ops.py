def add(x, y):
    return x+ y

def mult(x, y):
    return x* y

def subs(x, y):
    return x- y

def div(x, y):
    try:
        return x/ y
    except ZeroDivisionError as e:
        return str(e)
