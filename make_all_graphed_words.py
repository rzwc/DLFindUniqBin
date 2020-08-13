# Program used to create a text file of all possible di/tri or quadgraphs of the alphabet
import sys
import string 

def graphwords(number):
	
	# input used to determine which graphs to product
	graph = int(number)	

	alphabet_string = string.ascii_lowercase 	# returns all lowercase alphabetical characters 
	alphabet_list = list(alphabet_string)		# list of all lowercase alphabetical characters
	alphabet_length = len(alphabet_list)		# length of alphabet
	
	graphset = set() 	# set used to store graphed words
	firstindex = 0		# index for first character 
	
	# nested loop to create graphs depending on number inputted
	# loop through every alphabetical character for first character
	while firstindex < alphabet_length:
		str = ''
		str += alphabet_list[firstindex]
		secondindex = 0	# index for second character
		
		# loop through every alphabetical character for second character
		while secondindex < alphabet_length:
			# used first index to get first character
			str = alphabet_list[firstindex]
			# add second chracter
			str += alphabet_list[secondindex]
			thirdindex = 0		# index for third character
			
			# enter loop if trigraph and quadgraph because of third character
			if graph == 3 or graph == 4:
				# loop through every alphabetical character for third character 
				
				while thirdindex < alphabet_length:
					# create the string so far
					str = alphabet_list[firstindex] + alphabet_list[secondindex]
					# add third character
					str += alphabet_list[thirdindex]
					fourthindex = 0 	# index for fourth character
					
					# loop if quadgraph for fourth character
					if graph == 4:
						# loop through every alphabetical character for fourth character
						
						while fourthindex < alphabet_length:
							# create the string so far
							str = alphabet_list[firstindex] + alphabet_list[secondindex] + alphabet_list[thirdindex]
							# add fourth character
							str += alphabet_list[fourthindex]
							
							# reached loop for quadgraph, add to graph set
							graphset.add(str)	#increment index
							fourthindex += 1
							
					# if trigraph, add to graph set
					if graph ==3:
						graphset.add(str)
					thirdindex += 1	# increment index
					
			# if digraph, add to graph set
			if graph == 2:
				graphset.add(str)
			secondindex += 1 	# increment index
			
		firstindex += 1	# increment index 
	
	filename = ""

	# open corresponding graph file
	if graph == 2:
		filename = "all_digraphs.txt"
	elif graph == 3:
		filename = "all_trigraphs.txt"
	elif graph == 4:
		filename = "all_quadgraphs.txt"
	
	file = open(filename, "w")	
    	
    	# for every item in graph set, store in text file
	for x in graphset:
        	file.write(x + '\n')   
	file.close()

if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} 2 or 3 or 4 (2 for digraphs, 3 for trigraphs, 4 for quadgraphs)', file=sys.stderr)
		sys.exit()
    # run graphwords on first argument
	graphwords(sys.argv[1])
