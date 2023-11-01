
def prime(x):
    if x < 2:
        print("Not a prime.... number")
        return
    for i in range(2, x):
        if x % i == 0:
            print("Not a prime number")
            return

    print("Prime number")


prime(29)
