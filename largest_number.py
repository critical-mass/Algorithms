list = [1, 27, 3, 4, 5]

def largest_number(list):
    #empty list
    if list == []:
        return 0
    else:
        l = largest_number(list[1:])
        return l if l > list[0] else list[0]

print(largest_number(list))
