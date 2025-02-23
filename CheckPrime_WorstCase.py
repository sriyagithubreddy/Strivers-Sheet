# Function to check if a number is prime
def checkPrime(n):
    cnt = 0  # Counter to count factors of n

    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        if n % i == 0:  # If i is a divisor of n
            cnt += 1  # Increment the counter

    # If n has exactly 2 factors (1 and n itself), it's prime
    if cnt == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 1483  # Number to check
    isPrime = checkPrime(n)  # Call function to check if n is prime
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
