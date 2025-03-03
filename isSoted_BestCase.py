def isSorted(arr, n):
    # Start from the second element (index 1) and iterate through the array
    for i in range(1, n):
        # Compare the current element with the previous one
        # If the current element is smaller than the previous element, the array is not sorted
        if arr[i] < arr[i - 1]:
            return False  # Return False if the array is not sorted
        
    # If the loop completes without returning False, the array is sorted
    return True  # Return True if no elements were found that violate the sorted order
