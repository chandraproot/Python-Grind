# this program finds nth fibonacci series numvber withour recursion
pv1 = 0
pv2 = 1
curr = None

n = 9
for i in range(2, n+1):
    if n == 0:
        print("0")
    elif n == 1:
        print("1")
    else:
        fib = pv1 + pv2
        pv1 = pv2
        pv2 = fib


print(pv2)
