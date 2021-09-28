def syserror():
    raise SystemExit(1)

def inc(x):
    """
    Takes an integer value and returns an incremented value
    """
    return x+1

def add(x,y):
    """Add Function"""
    return x+y

def subtract(x,y):
    """Subtract Function"""
    return x-y

def multiply(x,y):
    """Multiply Function"""
    return x*y

def divide(x,y):
    """Divide Function"""
    return x/y

def flex_add(a, b):
    """
    Takes two arguments and adds them together and adapts to strings and types
    
    return
    ------
    addition or contatentation
    """
    
    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)
    else:
        try:
            return a+b
        except Exception as err:
            print(f"unexpected error has occured! -- {err}")