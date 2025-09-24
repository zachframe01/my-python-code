''' 
#learning: Advanced String Formatting

#color_name with a width of 12 characters,
#  left-aligned, and with the fill character "="
#the percent sign, "%"
#color_intensity with a width of 
# 12 characters, centered, and with 
# the fill character "="



item_name = input("type something:")


print(f"{item_name:+^12}")
print(f"{item_name:+>12}")

#new assignment


#Floating-point number air_temperature is read from input.
#  Use one print(f" ") statement to output "Temperature:
#  ", followed by air_temperature to 4 decimal places 
# and "C".

air_temperature = float(input("enter air temp:"))

print(f"Temperature: {air_temperature:.4f}C")
'''

#stripping whitespace

text = "   / hello world /   "
print(text)
print(text.strip())
