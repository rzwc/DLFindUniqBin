import sys

GRAPHNUMBER = 4

def split(word): 
    return [char for char in word]  

def graphwords(filename):
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
	graphedwordsset = set()
	while index < len(data): 
		currentword = data[index]
		charindex = 0
		if len(currentword) > GRAPHNUMBER:
			splitword = split(currentword) 
			while charindex < len(splitword) - (GRAPHNUMBER):
				str = ''
				graphindex = 0
				while graphindex < GRAPHNUMBER:
					str = str + splitword[charindex + graphindex] 
					graphindex += 1
				graphedwordsset.add(str.lower())
				charindex += 1
		else:
			graphedwordsset.add(data[index].lower())
		index += 1
		
	# open diff.txt to write
	file = open("quadgraphedwords.txt", "a")	
    	
    	# for every item in diff set, store in diff.txt
	for x in graphedwordsset:
        	file.write(x + '\n')   
	file.close()
	
if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	graphwords(sys.argv[1])
