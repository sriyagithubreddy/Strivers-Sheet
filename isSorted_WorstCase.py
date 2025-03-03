def isSorted(arr, n):
    # Outer loop to iterate over each element of the array
    for i in range(n):
        # Inner loop to compare the element at 'i' with every element that comes after it
        for j in range(i + 1, n):
            # If any element 'arr[j]' is smaller than the element 'arr[i]',
            # it means the array is not sorted in non-decreasing order
            if arr[j] < arr[i]:
                return False

    # If no such pair was found, it means the array is sorted
    return True
