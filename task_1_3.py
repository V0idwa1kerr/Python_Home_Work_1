i = 0
numbers = {11, 12, 13, 14}

for i in range(101):
    if i in numbers:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif (i % 10 > 1) and (i % 10 < 5):
        print(i, "процента")
    else:
        print(i, "процентов")
