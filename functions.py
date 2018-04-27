x = 100

def myfunc():
	global x 
	x = 25

	y = 'i am local to myfunc()'

	def insidefunc():
		print(x)
		nonlocal y
		y = 'I am getting changed in insidefunc()'
		print(y)

	insidefunc()
	print(y)


myfunc()
print(x)
