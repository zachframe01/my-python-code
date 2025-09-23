'''Write a program that takes in a line of text as input, 
and outputs that line of text in reverse.
The program repeats, ending when the user enters
 "Done", "done", or "d" for the line of text.'''

'''
#this block will set x to true or false.  
usr_str = input("enter your input: ")
if usr_str.lower() in [ "done" , "d" ] :
    x = True
else:
    x= False

#if x is true, end it
#if x is false, print it in reverse. 

if x == True :
    print("all done")
elif x == False : 
    for char in reversed(usr_str) : 
        print(char)
    break '''

while True:
    usr_str = input("enter your input: ")
    if usr_str.lower() in ["done", "d"]:
        break  # this exits the loop (program ends)
    else:
        print(usr_str[::-1])


    