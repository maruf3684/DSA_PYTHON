
s = 3749

def int_to_roman(num):
    roman_map = {
        1000: "M",
        2000: "MM",
        3000: "MMM",
        900: "CM",
        800: "DCCC",
        700: "DCC",
        600: "DC",
        500: "D",
        400: "CD",
        300: "CCC",
        200: "CC",
        100: "C",
        90: "XC",
        80: "LXXX",
        70: "LXX",
        60: "LX",
        50: "L",
        40: "XL",
        30: "XXX",
        20: "XX",
        10: "X",
        9: "IX",
        8: "VIII",
        7: "VII",
        6: "VI",
        5: "V",
        4: "IV",
        3: "III",
        2: "II",
        1: "I"
    }



    thousand_part = (num // 1000) * 1000
    num = num % 1000
    hundred_part = (num // 100) * 100
    num = num % 100
    ten_part = (num // 10) * 10
    num = num % 10
    unit_part = num


    ans = ""
    ans += roman_map[thousand_part] if thousand_part else ""
    ans += roman_map[hundred_part] if hundred_part else ""
    ans += roman_map[ten_part] if ten_part else ""
    ans += roman_map[unit_part] if unit_part else ""

    return ans

print(int_to_roman(s))
