try:
	a =int(input("Number1:"))
	b =int(input("Number2:"))
	c =int(input("Number3:"))
except:
	print("Error")
	exit()
def max_number(num1,num2,num3):
	if num1 > num2 and num1 > num3 :
		print("maximum number:",num1)
	elif num2 > num3 :
		print("maximum number:",num2)
	else :
		print("maximum number:",num3)
max_number(a,b,c)
