### Zachary - Frame - assignment2 - RatePay 
### name: Frame, Zachary   
### date: 9/15/2025
### description: create overtime pay calculations using a function for the calculation

def computepay(hours, rate):
    if hours > 40:
        reghrs = 40
        othrs = hours - 40
    else:
        othrs = 0
        reghrs = hours
    pay = reghrs * rate + othrs * rate * 1.5
    return(pay)

#input from user, hours and pay. convert the answers to float. 
hrs = input("input hours:")
rt = input("input pay (hourly):")
hours = float(hrs)
rate = float(rt)

###compute the pay 
print("your pay is:", (computepay(hours, rate)))