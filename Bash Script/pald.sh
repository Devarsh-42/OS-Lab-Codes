echo "Enter the number:"
read a

if [[ ! $a =~ ^[0-9]+$ ]]
then
	echo "Please enter a valid positive integer number."
	exit 1
fi

rev=$(echo $a | rev)

if [ $a == $rev ]
then
	echo "Your given number ${a} is a Palindrome."
else
	echo "Your given number ${a} is not a Palindrome."
fi
