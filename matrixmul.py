a=input("enter the rows")
b=input("enter the columns of 1")
c=input("enter the rows of 2")
d=input("enter the columns of 2")
l=[]
for i in range (0,a):
	e=[]
	for j in range (0,b):
		z=input("enter the elements")
		e.append(z)
	l.append(e)
m=[]
for i in range (0,c):
	k=[]
	for j in range (0,d):
		x=input("enter the elements")
		k.append(x)
	m.append(k)
print l
print m
z=[]
if (b==c):
	for i in range(a):
		h=[]
		for j in range(d):
			s=0
			for k in range(b):
				s=s+l[i][k]*m[k][j]
				h.append(s)
			z.append(s)
	print z
else:
	print "matrix multiplicational is not possible"

