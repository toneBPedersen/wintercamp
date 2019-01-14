color = "dark brown"

def bark(num):
    if num==0:
        return
    else:
        print("Woff")
        return bark(num-1)
