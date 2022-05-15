"""
    In a nutshell, this search algorithm takes advantage of a collection of elements
     that is already sorted by ignoring half of the elements after just one comparison. 

1.Compare x with the middle element.
2.If x matches with the middle element, we return the mid index.
3.Else if x is greater than the mid element, then x can only lie in the 
    right (greater) half subarray after the mid element. Then we apply the algorithm 
    again for the right half.
4.Else if x is smaller, the target x must lie in the left (lower) half. 
    So we apply the algorithm for the left half.
                                                """

def binarySearch(elementToFind,listOfElements):
    high = len(listOfElements)-1
    low = 0
    mid = 0

    while low<=high:
        mid = (low+high)//2
        if listOfElements[mid] == elementToFind:
            return mid
        if listOfElements[mid]>elementToFind:
            high = mid-1
        if listOfElements[mid]<elementToFind:
            low = mid+1   
    return -1

#Verify Above Algo
indexofElement = binarySearch(5, [1,2,3,5,6,7,8,10,11,12])
print(indexofElement)