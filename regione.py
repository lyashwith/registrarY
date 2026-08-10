print("Program to take input and assign roll number ranging from A-1 to Z-1000")
print("and output the name or roll number by the other value")
o={}
b={}
n=False
print("Press Enter to submit or quit from loop")
print()
print("Enter values here")
for i in range(65,91):
	j=chr(i)
	if n=="":
		break
	for k in range(1,1001):
		l=str(k)
		m=j+"-"+l
		n=input()
		if n=="":
			break
		print(m,":",n)
		o[m]=n
		b[n]=m
print("Enter N for name and R for roll number")
will=False
while will<1:
	a=input("Search for values by Names(N) or Roll number(R)? :")
	if a=="R" or a=="r":
		a1=input("Input the Roll number: ")
		print(o[a1])
	elif a=="N" or a=="n":
		a2=input("Input the name: ")
		print(b[a2])
	elif a=="":
		break
abc=input("Do you want to print the items in dictionary?:(type y for yes) ")
if abc=="Y" or abc=="y":
	print(o)
