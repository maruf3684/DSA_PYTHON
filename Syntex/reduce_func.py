from functools import reduce

nums = [1,2,3,4]

x = reduce(lambda a,b:a+b, nums,1)

print(x)