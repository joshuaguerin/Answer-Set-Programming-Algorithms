import sys
from random import randint

upper_limit = 20
set_size = 10


randint(1, upper_limit)

print("value(", end="")
for i in range(1, set_size):
    print(randint(1, upper_limit), " ; ", sep="", end="")
print(randint(1, upper_limit), ").", sep="")


