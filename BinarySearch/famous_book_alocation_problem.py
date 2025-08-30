
books = [25,46,28,47,24]
student = 4

books = [1,2,4,7,8]
student = 2



def distribute(books,student,max_pages):
    count = 0
    pages = 0

    i = 0
    while i < len(books):
        if pages+books[i] <= max_pages:
            pages = pages+books[i]
            if i == len(books)-1:
                count+=1
            i+=1
        else:
            count+=1
            pages=0

    if count<student:
        return -1
    elif count>student:
        return 1
    else:
        return 0


def binary_search(books,student):
    low = max(books)
    high = sum(books)
    ans = 0

    while low<=high:
        mid = low + (high-low)//2
        condition_of_distribution = distribute(books,student,mid)
        if condition_of_distribution == 0 or condition_of_distribution == -1:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans






print(binary_search(books,student))


