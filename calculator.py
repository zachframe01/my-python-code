#this will do math to two user input numbers
import math

#this adds two numbers
def add(x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x,y):
    return x**y

print("you have 2 numbers type the action you would like to perform /" \
"\n 1 add \n 2 subtract \n 3 multiply \n 4 divide \n 5 power")

action = int(input())
print(action)

