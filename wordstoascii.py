import sys

def split(word): 
    return [char for char in word]  

def wordstoascii(filename):
	try:
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data]
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
		
	index = 0
	asciiset = set()
	while index < len(data):
		currentword = data[index]
		splitword = split(currentword)
		charindex = 0
		string = ""
		while charindex < len(splitword):
			ascii = ord(splitword[charindex])
			string += str(ascii)
			charindex += 1
		asciiset.add(string)
		index += 1
		
	file = open("asciicodewordstri.txt", 'a')
	
	for x in asciiset:
		file.write(x + '\n')
		
	file.close()
	
			
		

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
	wordstoascii(sys.argv[1])
