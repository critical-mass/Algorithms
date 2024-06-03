i = 4
def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)

countdown(i=i)
