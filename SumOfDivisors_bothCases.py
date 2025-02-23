import math

def sum_of_divisors(n):
    total_sum = 0  # This will store the total sum of all divisors for numbers 1 to n
    
    # Loop through each number i from 1 to n
    for i in range(1, n + 1):
        sum_divisors = 0  # This will store the sum of divisors for the current number i
        
        # Loop through all possible divisors from 1 to sqrt(i)
        for j in range(1, int(math.sqrt(i)) + 1):
            # If j is a divisor of i (i.e., i % j == 0)
            if i % j == 0:
                sum_divisors += j  # Add j to the sum of divisors
                
                # Check if j and i/j are different (i.e., not a perfect square)
                if j != i // j:
                    sum_divisors += i // j  # Add i / j to the sum of divisors
        
        total_sum += sum_divisors  # Add the sum of divisors of i to the total sum
    
    return total_sum  # Return the total sum

# Example input
n = 4
print(sum_of_divisors(n))  # Output: 15
