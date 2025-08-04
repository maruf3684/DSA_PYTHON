arr = [12,0,1,2,3,4,5,6,8]

fast = 0
big = float('-inf')
second_big = float('-inf')

while fast < len(arr):
    if arr[fast] >= big:
        second_big = big
        big = arr[fast]
    elif second_big < arr[fast]:
        second_big = arr[fast]

    fast += 1

print(big)
print(second_big)

