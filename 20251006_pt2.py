print("I will give you a number to 5")

number = int(input("gimme a number: "))
while number <= 5:
    print(number)
    if number <= -10:
        print('thats too long!')
        break
    number += 1 

print("all done")
    

