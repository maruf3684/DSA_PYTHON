from traceback import format_list

arr1= [0,6,7,8,9,10]
arr2 = [0,1,2,3,4,5]


little_element = arr1[0]
second_little_element = None

if arr2[0] < arr1[0]:
    little_element = arr2[0]


for i in range(len(arr1)):
    if arr1[i] > little_element:
        second_little_element = arr1[i]
        break

for i in range(len(arr2)):
    if arr2[i] < second_little_element and arr2[i] != little_element:
        second_little_element = arr2[i]
        break

print(second_little_element)



