from loggit import loggit

@loggit()
def plus(a, b):
    return a + b

@loggit()
def minux(a, b):
    return a - b

@loggit()
def multiply(a, b):
    return a * b

@loggit()
def divide(a, b):
    return a / b