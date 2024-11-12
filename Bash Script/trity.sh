echo "Enter first side of triangle:"
read a
echo "Enter second side of triangle:"
read b
echo "Enter third side of triangle:"
read c

if [ $a == $b ] && [ $b == $c ]
then
	echo "The triangle is EQUILATERAL."
elif [ $a == $b ] || [ $b == $c ] || [ $c == $a ]
then
	echo "The triangle is ISOSCELES."
else
	echo "The triangle is SCALENE."
fi

