import sys

ALPHABET = 26

def digraphwords(filename):
	try:
        # open binary file to read
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data] 

    # print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
		
	digraphset = set() 
	firstindex = 0
	while firstindex < ALPHABET:
		str = ''
		str += data[firstindex]
		secondindex = 0
		while secondindex < ALPHABET:
			str = data[firstindex] 
			str += data[secondindex]
			digraphset.add(str)
			secondindex += 1
		firstindex += 1
	# open diff.txt to write
	file = open("all_digraphs.txt", "w")	
    	
    	# for every item in digraphset set, store in all_digraphs.txt
	for x in digraphset:
        	file.write(x + '\n')   
	file.close()

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} alphabet', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	digraphwords(sys.argv[1])
