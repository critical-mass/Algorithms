def findSmallest(arr):
    #set the smallest var to the first element in the list 
    smallest = arr[0]
    #set the smallets index to 0
    smallest_index = 0
    #for i in the range of 1 to the length of the array passed
    for i in range(1, len(arr)):
        #if the element i is less than the previously recorded element... 
        if arr[i] < smallest:
            #update smallest to be the elment (value) of i
            smallest = arr[i]
            #update smallest index to be the index of i (position) 
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    #set a blank array as placeholder. local var
    newArr = []
    #for i in the index of the array 
    for i in range(len(arr)):
        #find the smallest element in the array and return the index
        smallest = findSmallest(arr)
        #remove the smallest element from the initial list and append it to the new array
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([3, 9, 14, 2, 6]))