echo "Enter first number:"
read a
echo "Enter second number:"
read b
if [ ${a} > ${b} ]
then
	echo "${a} is greater number than ${b}."
elif [ ${a} == ${b} ]
then
	echo "${a} and ${b} are equal."
else
	echo "${b} is greater than ${a}."
fi

