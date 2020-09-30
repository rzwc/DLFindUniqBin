# program used to strip all nonalphanumeric character from text file
import sys 

# return list of characters from a string 
def split(word): 
    return [char for char in word] 
    
# return true if alphanumeric character
def isalphanumeric(b):
	return ord(b) >= ord('0') and ord(b) <= ord('9') or ord(b) >= ord('A') and ord(b) <= ord('Z') or ord(b) >= ord('a') and ord(b) <= ord('z')

def strip(filename):
	try:
		# open text file to read
		f = open(filename, 'r')
		# store each line in data 
		data = f.readlines()
		# strip \n
		data = [x.strip() for x in data]
		
	except IOError as e:
		# IOError
		print(f'{filename}: {e.strerror}', file = sys.stderr)
		
	# set to store striped alphanumeric strings
	striped_set = set()
	# loop through data, split into characters, remove nonalphanumeric and concatenate characters in a new string 
	for x in data:
		tostrip = split(x)	# tostrip stores list of characters to be striped of alphanumeric characters
		# index to loop through all characters of split string
		y = 0
		
		# loop through all characters of split string
		while y < len(tostrip):
			# if character is not alphanumeric character, remove from set
			if isalphanumeric(tostrip[y]) == False:
				tostrip.remove(tostrip[y])
			# if alphanumeric, move onto next index
			else: 
				y += 1
				
		# index to loop through list of characters
		charindex = 0
		string = ""	# intialize string
		
		# combine character ro form stirng
		while charindex < len(tostrip):
			string += tostrip[charindex]
			charindex += 1
			
		# if stirng is not empty,  add to list	
		if string != '':
			striped_set.add(string)
	
	# open file
	file = open("striped" + f.name, 'w')
	
	# store set to file
	for x in striped_set:
		file.write(x + '\n')
		
	# close file
	file.close()
	

if __name__ == '__main__':
	# Usage format
	if len(sys.argv) != 2:
		print(f'Usage: python {sys.argv[0]} filename', file=sys.stderr)
	
	# run on first argument
	strip(sys.argv[1])
