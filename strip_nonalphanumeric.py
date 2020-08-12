import sys 

def split(word): 
    return [char for char in word] 
    
def isprint(b):
	return ord(b) >= ord('0') and ord(b) <= ord('9') or ord(b) >= ord('A') and ord(b) <= ord('Z') or ord(b) >= ord('a') and ord(b) <= ord('z')

def strip(filename):
	try:
		f = open(filename, 'r')
		data = f.readlines()
		data = [x.strip() for x in data]
		
	except IOError as e:
		print(f'{filename}: {e.strerror}', file = sys.stderr)
		
	index = 0
	striped_set = set()
	for x in data:
		striped = split(x)
		y = 0
		while y < len(striped):
			if isprint(striped[y]) == False:
				striped.remove(striped[y])
			else: 
				y += 1
		charindex = 0
		string = ""
		while charindex < len(striped):
			string += striped[charindex]
			charindex += 1
		if string != '':
			striped_set.add(string)
	
	file = open("stripedteststringsoutput.txt", 'w')
	
	for x in striped_set:
		file.write(x + '\n')
		
	file.close()
	

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print(f'Usage: python {sys.argv[0]} filename', file=sys.stderr)
	
	strip(sys.argv[1])
