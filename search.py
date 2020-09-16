#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


# [ant, bees, cat, dog] 
# target == cat
def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    elif array[index] != item:
        return linear_search_recursive(array, item, index +1)
    else:
        return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
# [1,2,3,4,5,6,7,8,9] find the middle item in array
    left = 0
    right = len(array) - 1

    while left <= right:
        # if middle item == item, return index of item
        # if item is less or greater than middle item, look left or right in array
        middle_index = (left + right) // 2

        if item == array[middle_index]: 
            return middle_index
        elif item < array[middle_index]:
            # move my pointers
            right = middle_index - 1
        elif item > array[middle_index]: 
            # move my pointers
            left = middle_index + 1

binary_search_iterative([1,2,3,4,5,6,7,8,9], 5)


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    
    middle_index = (left + right) // 2

    if item == array[middle_index]: #base case
        return middle_index
    if left >= right: #2nd base case
        return None

    # recursive cases
    elif item < array[middle_index]:
        # move my pointers
        right = middle_index - 1
        return binary_search_recursive(array, item, left, right)

    elif item > array[middle_index]: 
        # move my pointers
        left = middle_index + 1
        return binary_search_recursive(array, item, left, right)
