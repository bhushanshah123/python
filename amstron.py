n=int(input())
s=0
t=n
while (n>0):
	d=n%10
	s=s+(d**3)
	n=n//10
if (t==s):
	print("no is amstrong")
else :
	print("no is not amstrong")

