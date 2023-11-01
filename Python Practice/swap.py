given = [12, 35, 9, 56, 24]

out = []
for i in range(len(given)):
    index = given[-1]
    out.append(index)
    given.pop()
    # i = i + 1


print(out)
