# for i in range(25):
#     print(":)")

import math
from random import randint

print("can you guess my number ")
answer = randint(1, 1000)
while True:
    response = input()
    if int(response) == answer:
        print("Good job")
        break
    elif int(response) < answer:
        print("too low")
    elif int(response) > answer:
        print("too high")