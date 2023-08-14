def is_leap(year):
    leap = False

    # Write your logic here

    if year == 1900 or year == 1800 or year ==2100 or year == 2200 or year == 2300 or year == 2500:
        leap = True

    elif  year%4 ==0:
        leap = True
    elif year%4== 0 and year% 100 == 0:
        leap = False
    elif year%100== 0 and year %400 ==0 :
        leap = True
    else:
        leap = False

    return leap


year = int(input())
x = is_leap(year)
print(x)