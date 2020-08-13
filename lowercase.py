# Program used to turn all characters in a file to lowercase
import sys

def lowerwords(filename):
	try:
        # open text file to read
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data] 

    # print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
	
	index = 0	#index to track position in file
	lowercaseset = set()	#initialize set for lowercased words
	
	# loop through each line of text file, use lower() function to lowercase and add to new set
	while index < len(data):
		currentword = data[index].lower()
		lowercaseset.add(currentword)
		index += 1
	
	# open lowered{filename}.txt to write
	file = open("lowercased" + f.name, "a")	
    	
    	# for every item in diff set, store in diff.txt
	for x in lowercaseset:
        	file.write(x + '\n')   
	file.close()
	
		
if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run lower words on first argument
	lowerwords(sys.argv[1])
