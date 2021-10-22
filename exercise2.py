try:
	n=int(input("n-dy engiz:"))
except:
	print("San engiz")
	exit()

def func(a):
	i=1
	summa=0
	if n>0:
		while i<=n:
			num=1/i
			print(num)
			summa=summa+num
			i+=1
		return summa
	else:
		return -1
a=func(n)
print("Summa:",a)
