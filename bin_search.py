list = [1, 2, 3, 4, 5, 6]
target = 3

def bin_search(list, target):
    #define our high points and low points
    low = 0
    #subtrack 1 because lists start with a 0 point not a 1
    high = len(list)-1

    #While our low point is less than or equal to our high...
    while low <= high:
        #Define the middle by adding the high and low then dividing by 2 (//)
        #instead of regular division (/) to ensure that mid is an integer
        mid = (low + high) // 2
        #Define our guess then check if it's equal to our target
        guess = list[mid]
        #If it is, resolve the while loop.
        if guess == target:
            print(mid) 
        #If the guess is greater than the target, set our new high to be one 
        #position lower than the current mid 
        if guess > target:
            high = mid - 1 
        #If the guess was too low set a new low to be mid + 1
        else:
            low = mid + 1
    return None

bin_search(list=list, target=target)