"""
    A simple approach is to do linear search, i.e

    1.Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    2.If x matches with an element, return the index.
    3.If x doesn’t match with any of element
    """
def linearSearch(elementToFind,listOfElements):
    for element in listOfElements:
        if element == elementToFind:
            return listOfElements.index(element)
    return -1

#Verify Above Algo
indexofElement = linearSearch(5, [1,2,3,5,6,7,8,10,11,12])
print(indexofElement)