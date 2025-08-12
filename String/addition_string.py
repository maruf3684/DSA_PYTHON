num1 = "1"
num2 = "9"


def addition(num1, num2):
    big_one = None
    small_one = None

    if len(num1) > len(num2):
        big_one = num1
        small_one = num2
    else:
        big_one = num2
        small_one = num1

    i = len(big_one) -1
    j = len(small_one) -1
    carry = 0

    ans = []

    while i >= 0:
        from_big = ord(big_one[i]) - ord('0')
        from_small = 0
        if j >= 0:
            from_small = ord(small_one[j]) - ord('0')

        temp_ans = from_big + from_small + carry
        carry = temp_ans // 10
        put = temp_ans % 10
        ans.append(str(put))
        i-=1
        j-=1
    if carry > 0:
        ans.append(str(carry))

    return "".join(reversed(ans))



print(addition(num1, num2))

