a = []
for i in range(0,100):
	if len(a[i])%2==0:
		a.append(1)
	else:
		a.append(len(a[i])%5)
print(a)
