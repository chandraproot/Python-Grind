
from tkinter import *
Pr = float(input("Enter the principal amount: "))
Rate = float(input("Enter the rate of intrest: "))
time = float(input("Enter the time of the intrest:  "))


def simple_intrest(P, R, T):

    intrest = (P * R * T)/100
    print("The intrest is: ", intrest)


ints = simple_intrest(Pr, Rate, time)
