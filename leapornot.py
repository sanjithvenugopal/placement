# your code goes here
x=int(input())
if x%4==0:
	if x%100==0:
		if x%400==0:
			print("yes")
		else:
			print("no")
	else:
		print("yess")
else:
	print("not")
