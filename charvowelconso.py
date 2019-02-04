#sanjith
x=input()
if x.isalpha():
	y=x.lower()
	if y=='a' or y=='e' or y=='i' or y=='o' or y=='u':
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
