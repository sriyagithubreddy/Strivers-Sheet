class Solution {
  public:
    // Function to find the largest element in the array
    int largest(vector<int> &arr) {
        // Get the size of the input array
        int n = arr.size();
        
        // Initialize 'largest' to 0. This will store the largest element found.
        // Note: This works only if the array contains positive numbers. For an array with negative values, you should initialize 'largest' to a very small value (e.g., INT_MIN).
        int largest = 0; 
        
        // Loop through each element in the array
        for(int i = 0; i < n; i++) {
            // If the current element is greater than 'largest', update 'largest'
            if(arr[i] > largest) {
                largest = arr[i];
            }
        }
        
        // Return the largest element found
        return largest;
    }
};
