echo "Enter the number here:"
read n
a=0
b=1
echo "The Fibonacci series until your given number is:"
for (( i=0 ; i<n ; i++))
do
	echo -n " $a "
	fs=$((a+b))
	a=$b
	b=$fs
done

