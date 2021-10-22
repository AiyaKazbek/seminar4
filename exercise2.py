def func(n):
	i=1
	summa=0
	if n>0:
		while i<=n:
			num=1/i
			print(num)
			summa=summa+num
			i+=1
	return summa
a=func(3)
print("Summa:",a)
