x = 100

def test():
    global x
    x = 900
    print("Inside test:", x)

def z():
    print("Inside z:", x)

test()
z()