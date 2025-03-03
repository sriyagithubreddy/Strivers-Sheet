# User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # If the array has 1 or fewer elements, return -1 because there is no second largest element
        if len(arr) <= 1:
            return -1
        
        # Convert the array to a set to remove duplicates, then sort the unique elements
        x = sorted(set(arr))
        
        # If there are more than one unique element in the sorted list
        if len(x) > 1:
            # Return the second largest element, which is at the second last position
            return x[-2]
        else:
            # If there is no second largest element (i.e., all elements were the same), return -1
            return -1