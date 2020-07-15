import sys

def lowerwords(filename):
	try:
        # open binary file to read
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data] 

    # print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
	
	index = 0
	lowercaseset = set()
	
	while index < len(data):
		currentword = data[index].lower()
		lowercaseset.add(currentword)
		index += 1
	
	# open diff.txt to write
	file = open("loweredwords.txt", "a")	
    	
    	# for every item in diff set, store in diff.txt
	for x in lowercaseset:
        	file.write(x + '\n')   
	file.close()
	
		

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	lowerwords(sys.argv[1])
