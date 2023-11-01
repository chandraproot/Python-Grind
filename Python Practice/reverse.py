# string = "This is the string to be reversed"
string = "BanBanjara has the right to terminate this agreement at any point if it observes unsatisfactory performance. Only a one week notice would be served during this period."
re = string.split()
print(re)
l = len(re)
print(l)
new = []
for i in range(1, l+1):
    nw = re[-1]

    new.append(nw)

    re.pop()

print(new)
print(" ".join(new))
