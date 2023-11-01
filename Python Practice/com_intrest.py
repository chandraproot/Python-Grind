def compound_intrest(pr, r, t):
    amount = pr*(pow((1 + r/100),  t))
    intrest = amount - pr
    return intrest


my_intrest = compound_intrest(3000, 5, 3)
print(my_intrest)
