from loggit import loggit

@loggit()
def func(a, b):
    return a / b

def main():
    func(1, 2)
    func(1, 0)
    func(1, 1)

if __name__ == "__main__":
    main()