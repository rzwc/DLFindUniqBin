import sys
import string 

ALPHABET_LENGTH = 26

def graphwords(number):

	alphabet_string = string.ascii_lowercase
	alphabet_list = list(alphabet_string)
	graph = int(number)
		
	graphset = set() 
	firstindex = 0
	while firstindex < ALPHABET_LENGTH:
		str = ''
		str += alphabet_list[firstindex]
		secondindex = 0
		while secondindex < ALPHABET_LENGTH:
			str = alphabet_list[firstindex]
			str += alphabet_list[secondindex]
			thirdindex = 0
			if graph == 3 or graph == 4:
				while thirdindex < ALPHABET_LENGTH:
					str = alphabet_list[firstindex] + alphabet_list[secondindex]
					str += alphabet_list[thirdindex]
					fourthindex = 0
					if graph == 4:
						while fourthindex < ALPHABET_LENGTH:
							str = alphabet_list[firstindex] + alphabet_list[secondindex] + alphabet_list[thirdindex]
							str += alphabet_list[fourthindex]
							graphset.add(str)
							fourthindex += 1
					if graph ==3:
						graphset.add(str)
					thirdindex += 1
			if graph == 2:
				graphset.add(str)
			secondindex += 1
		firstindex += 1
	
	filename = ""

	# open diff.txt to write
	if graph == 2:
		filename = "all_digraphs.txt"
	elif graph == 3:
		filename = "all_trigraphs.txt"
	elif graph == 4:
		filename = "all_quadgraphs.txt"
	
	file = open(filename, "w")	
    	
    	# for every item in quadgraph set, store in all_quadgraphs.txt
	for x in graphset:
        	file.write(x + '\n')   
	file.close()

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} 2 or 3 or 4 (2 for digraphs, 3 for trigraphs, 4 for quadgraphs)', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	graphwords(sys.argv[1])
