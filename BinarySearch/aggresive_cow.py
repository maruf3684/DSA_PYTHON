#arr,k = [1, 2, 4, 8, 9],3
#arr,k = [10, 1, 2, 7, 5],3
#arr,k = [2, 12, 11, 3, 26, 7],5
arr,k = [1,5,17],2


def find_min_distance(arr,k):
    ans = None
    arr = sorted(arr)
    end = arr[-1] - arr [0]

    for i in range(1,end+1):
        possible = calculate_distance(arr,k,i)
        if possible:
            ans = i
    return ans


def find_min_distance_with_bin_s(arr,k):
    arr = sorted(arr)
    start = 1
    end = arr[-1] - arr [0]

    while start<=end:
        mid = start + (end-start)//2
        if calculate_distance(arr,k,mid):
            start=mid+1
        else:
            end = mid-1
    return end


def calculate_distance(arr,k,distance):
    sum = 0
    for index,item in enumerate(arr):
        if index == 0:
            sum=item
            k-=1
        else:
            length = sum+distance
            if length > item:
                pass
            else:
                k-=1
                sum=item

        if k == 0:
            return True
    return False



ans = find_min_distance(arr,k)
ans2 = find_min_distance_with_bin_s(arr,k)
print(ans)
print(ans2)




