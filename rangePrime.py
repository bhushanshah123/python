#in range find prime number
no1=int(input())
no2=int(input())
for n in range (no1,no2):
	s=0
	for i in range(1,n):	
		if (n%i==0):
			s=1
	if (s==1):
		print(s)

