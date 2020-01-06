verbose = True

def example1():
    if verbose:
        print('Running example1')

been_called = False

def example2():
    global been_called
    been_called = True



count = 0

def example3():
    global count
    count += 1



known = {0: 0, 1: 1}

def example4():
    known[2] = 1
    print(known)

def example5():
    #再代入では必要
    global known
    known = dict()


example1()
example3()
example4()