"""
instructions:Define a function called exact_change that takes the total change amount 
in cents and calculates the change using the fewest coins. The coin types are pennies, 
nickels, dimes, and quarters. Then write a main program that reads the total change amount
 as an integer input, calls exact_change(), and outputs the change, one coin type per line. 
 Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies. Output "no change" 
 if the input is 0 or less.

Ex: If the input is:

0 
(or less), the output is:

no change
Ex: If the input is:

45
the output is:

2 dimes 
1 quarter
Your program must define and call the following function. The function exact_change() should return a tuple containing num_pennies, num_nickels, num_dimes, and num_quarters.
def exact_change(user_total)

"""

def exact_change(user_total):
    # Calculate each coin type using // (floor division) and % (modulus)
    num_quarters = user_total // 25
    user_total %= 25

    num_dimes = user_total // 10
    user_total %= 10

    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total

    # Return results as a tuple
    return num_pennies, num_nickels, num_dimes, num_quarters


if __name__ == "__main__":
    input_val = int(input())

    if input_val <= 0:
        print("no change")
    else:
        num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

        # Print pennies first
        if num_pennies > 0:
            if num_pennies == 1:
                print("1 penny")
            else:
                print(f"{num_pennies} pennies")

        if num_nickels > 0:
            print(f"{num_nickels} nickel" + ("s" if num_nickels > 1 else ""))

        if num_dimes > 0:
            print(f"{num_dimes} dime" + ("s" if num_dimes > 1 else ""))

        if num_quarters > 0:
            print(f"{num_quarters} quarter" + ("s" if num_quarters > 1 else ""))

        