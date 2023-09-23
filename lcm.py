n1=int(input())
n2=int(input())
a=n1;
b=n2;
while (n1!=n2):
	if(n1>n2):
		n1=n1-n2;
	else:
		n2=n2-n1;
print(n1)
lcm=(a*b/n1)
print(lcm)
