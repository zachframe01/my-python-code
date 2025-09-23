# Define your function here 
#this function will take the laps of a highschooler
#then convert it into miles. 4 laps = 1 mile. 
def laps_to_miles (user_laps):
    return user_laps * .25


if __name__ == "__main__":
    # Type your code here. Your code must call the function. 
    print (f"{laps_to_miles(float(input('Enter your laps: '))):.2f}")