def fibbo(num):
    if num == 0:
        return 0
    elif num==1:
        return 1
    else:
        return fibbo(num-1)+fibbo(num-2)

fibbo_3 = fibbo(3)
print(fibbo_3)