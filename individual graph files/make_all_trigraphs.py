import sys
import string

ALPHABET_LENGTH = 26

def trigraphwords():
	
	alphabet_string = string.ascii_lowercase
	alphabet_list = list(alphabet_string)
		
	trigraphset = set() 
	firstindex = 0
	while firstindex < ALPHABET_LENGTH:
		str = ''
		str += alphabet_list[firstindex]
		secondindex = 0
		while secondindex < ALPHABET_LENGTH:
			str = alphabet_list[firstindex]
			str += alphabet_list[secondindex]
			thirdindex = 0
			while thirdindex < ALPHABET_LENGTH:
				str = alphabet_list[firstindex] + alphabet_list[secondindex]
				str += alphabet_list[thirdindex]
				trigraphset.add(str)
				thirdindex += 1
			secondindex += 1
		firstindex += 1
	# open diff.txt to write
	file = open("all_trigraphs.txt", "w")	
    	
    	# for every item in trigraph set, store in all_trigraphs.txt
	for x in trigraphset:
        	file.write(x + '\n')   
	file.close()

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 1:
		print(f'Usage: python3 {sys.argv[0]}', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	trigraphwords()
