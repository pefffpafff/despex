from random import randint
A10 = []
for i in range(10):
	n = randint(-10,50)
	#print(n)
	A10.append(n)
print(A10)
x = 0
for i in A10:
	if i % 2 != 0 and i > 0:
		x = x + i

print(x)

