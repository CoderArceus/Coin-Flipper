import random
try:
	inp1 = int(input('how many times? '))
except ValueError:
	print('Invalid Input')
	
heads = 0
tails = 0
times = range(inp1)

for i in times:
	rand = random.randint(0, 1)
	if rand == 0:
		heads += 1
	else:
		tails += 1
		
print('You got ' + str(heads) + ' heads and ' + str(tails) + ' tails out of ' + str(inp1) + ' times flipped')
