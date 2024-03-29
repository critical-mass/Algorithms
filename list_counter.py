list = [1, 2, 3, 4, 5]

def list_counter(list):
    #empty list
    if list == []:
        return 0
    #calling itself
    else:
        return 1 + list_counter(list[1:])

print(list_counter(list))
