import sys

ALPHABET = 26

def trigraphwords(filename):
	try:
        # open binary file to read
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data] 

    # print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
		
	trigraphset = set() 
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
				trigraphset.add(str)
				thirdindex += 1
			secondindex += 1
		firstindex += 1
	# open diff.txt to write
	file = open("alltrigraphs.txt", "a")	
    	
    	# for every item in diff set, store in diff.txt
	for x in trigraphset:
        	file.write(x + '\n')   
	file.close()

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	trigraphwords(sys.argv[1])
