# import math

# print(math.sqrt(16))
# print(math.factorial(5))

# from math import sqrt

# print(math.sqrt(16))

# import math as a

# print(a.sqrt(16))

# import random as r

# print(r.randint(1,10))
import requests
icerik = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(icerik.json())