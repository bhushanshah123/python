#in range find perfect number
no1=int(input())
no2=int(input())
for n in range (no1,no2):
	s=0
	for i in range (1, n):
		if (n%i==0):
			s=s+i
	if (n==s):
		print (n)

