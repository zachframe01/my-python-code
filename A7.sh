\#!/bin/bash
#this script will display the users username, ID, and home derectory.
#it will backup the provided input to a given directory
# it will calculate a equation given 2 inputs
# it iwll read a string and count the number of words.
# it will also save the result to a file as well as displaying it to the scree
USER2=$(whoami)

echo "username: $USER2"
echo "ID : $(id -u)"
echo "home dir: $HOME"


# this will be the back up

echo "what file would you like backed up?"
read file
echo "what dir would you like it to go to?"
read dir
#check if the source file exists
if test -f "$file"; then
	#check if the dir exists
	if test -d "$dir"; then	
		echo "completeing backup"
		cp -v "$file" "$dir/"
		echo "backup complete"
	else
		echo "bad dir name"
	fi
else
	echo"bad file name"
fi



#this will combine 2 user input numbers. 

echo "give me two numbers"
read num1
read num2
result=$(($num1+$num2))
echo "$num1+$num2=$result"

# this will count the words and save it to word count file
echo "give me a sentence and I will count the words and save it to count.txt"

read userstring

wordcount=$(echo "$userstring" | wc -w)
product=$(echo "word count is: $wordcount") 
echo $product
echo $product > A7.txt

