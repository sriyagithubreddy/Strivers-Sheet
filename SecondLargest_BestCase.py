class Solution:
    def getSecondLargest(self, arr):
        # Convert the list to a set to remove duplicate elements, then sort the set
        arr = sorted(set(arr))
        
        # If the array has 1 or fewer unique elements, return -1 because there is no second largest element
        if len(arr) <= 1:
            return -1
        else:
            # Return the second largest element, which is at the second-to-last position
            return arr[-2]