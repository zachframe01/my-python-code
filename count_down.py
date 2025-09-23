'''x = int(input("enter your number"))
if x == (9,99):

    while x >= 0:
        print (x)
        x = (x - 1)
else:
    print("enter right number")
'''

"""Simple countdown script.

Prompts the user for an integer between 9 and 99 (inclusive) and counts down to 0.
"""

# Get input from person

num = int(input("Enter an integer (11-99): "))

# Check input range
if num < 11 or num > 99:
    print("Input must be 11-99")
else:
    # Countdown loop
    while True:
        print(num)

        # Split number into tens and ones
        tens = num // 10
        ones = num % 10

        # Stop if both digits are the same
        if tens == ones:
            break

        # Decrement number
        num -= 1