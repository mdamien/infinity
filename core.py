import random

def add_link(x):
	if random.randint(0,10) == 1:
		x = '<a href="/{x}">{x}</a>'.format(x=x)
	if random.randint(0,100) == 1:
		x = x+"<br/>"
	elif random.randint(0,60) == 1:
		x = "</p><h{n}>{x}</h{n}><p>".format(x=x,n=random.randint(1,3))
	return x

def generate(x):
	random.seed(x)
	words = [x.strip() for x in open('words')]
	return ' '.join(map(add_link,[random.choice(words) for x in xrange(random.randint(300,400))]))
	
if __name__ == "__main__":
    print(generate("dadamien"))
