
def big_factorial_2(n):
    ans = 1
    while n > 0:
        ans *= n
        n -= 1
    return ans
print(big_factorial_2(120))




def big_factorial(n):
    given_number = n
    ans = []

    while given_number != 0:
        cutting = given_number % 10
        remaining = given_number // 10
        ans.append(cutting)
        given_number = remaining

    start_from = n-1
    len_of_ans = len(ans)
    while start_from >= 1:
        remaining = 0
        for i in range(len_of_ans):
            temp = ans[i] * start_from + remaining
            cutting = temp % 10
            remaining = temp // 10
            ans[i] = cutting

        while remaining != 0:
            cutting = remaining % 10
            remaining = remaining // 10
            ans.append(cutting)

        len_of_ans = len(ans)
        start_from-=1
    return "".join(map(str, reversed(ans)))

print(big_factorial(120))



