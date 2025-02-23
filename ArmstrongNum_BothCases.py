# Function to check if a number is an Armstrong number
def isArmstrong(num):
    # Get the number of digits in the number
    k = len(str(num))
    # Initialize sum to 0
    sum = 0
    # Copy the number to a temporary variable
    n = num
    # Loop through each digit of the number
    while n > 0:
        # Get the last digit
        ld = n % 10
        # Add the digit raised to the power of k to the sum
        sum += ld ** k
        # Remove the last digit
        n = n // 10
    # Check if the sum equals the original number
    return sum == num

def main():
    number = 153
    # Check if the number is an Armstrong number
    if isArmstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")

if __name__ == "__main__":
    main()
