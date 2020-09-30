import sys

UNICODE0 = 48

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
		
	#index = 0
	#asciiset = set()
	#while index < len(data):
	#	currentword = data[index]
	#	splitword = split(currentword)
	#	charindex = 0
	#	string = ""
	#	while charindex < len(splitword):
	#		ascii = ord(splitword[charindex])
	#		string += str(ascii)
	#		charindex += 1
	#	asciiset.add(string)
	#	index += 1
	
	index = 0
	asciiset = set()
	while index < len(data):
		currentword = data[index]
		splitword = split(currentword)
		charindex = 0
		string = ""
		char = ord(splitword[charindex]) - UNICODE0
		charindex += 1
		#print(currentword)
        
		while charindex < len(splitword) + 1:
			if char < 0:
				sign = 1
			else:
				sign = 0
			value = (sign << 7)|abs(char)
			print("char:" + str(char) + " value:" + str(value))
            
			string += str(bytes([value]))
			
			if charindex < len(splitword):
				char = ord(splitword[charindex - 1])
				nextchar = ord(splitword[charindex])
				char = int(nextchar) - int(char)
			charindex += 1
		
		if len(splitword) == 1:
			if char < 0:
				sign = 1
			else:
				sign = 0
			value = (sign << 7)|abs(char)
			asciiset.add(str(bytes([value])))

		asciiset.add(string)
		index += 1
		
	file = open("ascii_coded_" + f.name, 'w')
	print(bytes([(1 << 7)|abs(50)]))
	print(128|50)
	print(0|30)
	print(1 << 7)
	print(bin(30))
	
	for x in asciiset:
		file.write(x + '\n')
		
	file.close()
	
			
		

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
	wordstoascii(sys.argv[1])
