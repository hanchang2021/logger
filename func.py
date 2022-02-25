from loggit import loggit

@loggit(log_res=True)
def plus(a, b):
    return a + b

@loggit(log_time=True, log_res=True)
def minus(a, b):
    import time
    time.sleep(1)
    return a - b

@loggit()
def multiply(a, b):
    return a * b

@loggit()
def divide(a, b):
    return a / b