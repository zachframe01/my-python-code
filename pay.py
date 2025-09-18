hourly_pay = float(input("Enter Rate:"))
hours_worked = float(input("Enter hours:"))
pay = hourly_pay * hours_worked

if hours_worked > 40.0 :
    reg_pay = 40 * hourly_pay #this is how much you got paid for 40 hours of work
    overtime = hours_worked - 40 # this is how many hours you worked overtime
    overtime_pay = (overtime * ( hourly_pay * 1.5 ))  # calculates the pay for ONLY overtime
    pay2 = reg_pay + overtime_pay #adds the overtime and regular pay
    print('your pay is', pay2, 'dollars! You worked overtime!')
else :
     print (' you made ', pay, 'dollars')
