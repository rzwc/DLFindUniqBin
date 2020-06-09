import sys

MINLEN = 4

def isprint(b):
	return b >= ord(' ') and b <= ord('~') or b == ord('\t')

def strings(filename):
	try:
		f = open(filename, 'rb')
		data = f.read()
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()

	###
	# print(len(data), type(data), isprint(data[0]), isprint(data[1]))
	###
	# user/share/dict/words english words/spell checker
	# diff of strings and stringlish for types of patterns to reject
	# script to compute diff of strings and stringlish and take out
	# compare sets, iterate through one 
	
	
	x = 0
	last = 0
	while x < len(data) - 4: 
		last = x
		if isprint(data[x]) == True:
			start = x
			counter = 0
			bool = 0
			length = 0
			while counter < MINLEN:
				if isprint(data[x]) == True:
					length = length + 1
				x = x + 1
				counter = counter + 1
			if length >= MINLEN:
				bool = 1
			
			x = start
			
			while bool == 1:
				print(chr(data[x]), end = "")
				if isprint(data[x+1]) == False:
					last = x 
					bool = 0
					print()
				x = x + 1
		x = last + 1
	f.close()
	
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
	strings(sys.argv[1])
