from loggit import loggit

@loggit
def func(a, b):
    return a + b

def main():
    func(1, 2)

if __name__ == "__main__":
    main()