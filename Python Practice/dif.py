


# Define your function
def f(x):
    return 2*x**3 + 9*x**2 + 7*x -6

# Calculate the derivative symbolically
def df(x):
    return 6*x**2 + 18*x +7

# df now contains the symbolic derivative of f
# print(df)
value = df(1)
# print(value)

val = 0.51 - f(0.51)/df(0.51)
print(val)

