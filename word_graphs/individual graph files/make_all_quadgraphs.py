import sys

ALPHABET = 26

def quadgraphwords(filename):
	try:
        # open binary file to read
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data] 

    # print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
		
	quadgraphset = set() 
	firstindex = 0
	while firstindex < ALPHABET:
		str = ''
		str += data[firstindex]
		secondindex = 0
		while secondindex < ALPHABET:
			str = data[firstindex]
			str += data[secondindex]
			thirdindex = 0
			while thirdindex < ALPHABET:
				str = data[firstindex] + data[secondindex]
				str += data[thirdindex]
				fourthindex = 0
				while fourthindex < ALPHABET:
					str = data[firstindex] + data[secondindex] + data[thirdindex]
					str += data[fourthindex]
					quadgraphset.add(str)
					fourthindex += 1
				thirdindex += 1
			secondindex += 1
		firstindex += 1
	# open diff.txt to write
	file = open("all_quadgraphs.txt", "w")	
    	
    	# for every item in quadgraph set, store in all_quadgraphs.txt
	for x in quadgraphset:
        	file.write(x + '\n')   
	file.close()

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} alphabet', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	quadgraphwords(sys.argv[1])
