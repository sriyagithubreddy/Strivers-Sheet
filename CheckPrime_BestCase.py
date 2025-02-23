import math

# Function to check if a number is prime
def checkPrime(n):
    cnt = 0  # Counter for divisors of n

    # Loop through numbers from 1 to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If i divides n evenly
            cnt += 1  # Increment the divisor count

            # If i and n/i are different, count n/i as well
            if n // i != i:
                cnt += 1

    # If there are exactly two divisors (1 and n), it's prime
    if cnt == 2:
        return True  # Prime
    else:
        return False  # Not prime

# Main function
def main():
    n = 1483  # Number to check
    isPrime = checkPrime(n)  # Check if n is prime
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

if __name__ == "__main__":
    main()
