#a bunch of random imports
from lark import Lark, Transformer, Visitor
import math 
import itertools
import time
import random
var = 1
one = "1"
true = False
test = test.test()
#functions that use some of those imports
def wait_seconds (seconds):
    time.sleep(seconds)

def generate_random_numbers(amount):
    numbers = []
    for number in range(amount):
        numbers.append(random.randint(0,100))
# a nested if statement
if True == "string":
    if False == 1:
        print("hello")

#decorator example
@decorator.test()
def decorator_function():
    pass
