
# 1) Format strings with f-Strings
name = 'Alex'
my_string = f"Hello {name}"
print(my_string)

i = 10
print(f"{i} sqaured is {i*i}")


# 2) Merge two dictionaries 

d1 = {"name" : 'Alex', 'age' : 25}
d2 = {"name" : 'Alex', 'city' : 'New York'}
merged_dict = {**d1, **d2}
print('Merged dictionaries: ', merged_dict)

# 3) Save Memory with Generators 
import sys
from time import time

t0 = time()
my_list = [i for i in range(10000)]
print(sum(my_list))
print('Duration of using list comprehension: ', round(time() - t0, 3), 's')
print('Size of my list: ', sys.getsizeof(my_list), 'bytes')

my_gen = (i for i in range(10000))
print(sum(my_gen))
print('Size of my generator: ', sys.getsizeof(my_gen), 'bytes')


# 4) Simplify if statement for multiple checks
colors = ['red', 'green', 'blue']
c = 'red'
if c == 'red' or c == 'green' or c == 'blue':
	print("is main color")

if c in colors:
	print('is main color')


# 5) Variable Assignment 
x, y, z = 1, 2, 3
x, *y = 1, 2, 3, 4, 5
print(f"x = {x}")
print(f"y = {y}")






