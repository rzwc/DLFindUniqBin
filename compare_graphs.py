# Program used to compare all possible (di/tri/quad)graphs to the (di/tri/quad)graphs found
import sys

def comparegraphs(foundgraphs, allgraphs):
	try:
        # open text file to read
		f = open(foundgraphs, 'r')
        # store each line of text file in data, remove \n
		data = f.readlines()
		data = [x.strip() for x in data] 
		
        # open text file to read 
		f = open(allgraphs, 'r')
        # store each line of text file in alldata, remove \n
		alldata = f.readlines()
		alldata = [x.strip() for x in alldata] 
		
	# print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
	
    # index to track the set of all graphs
	allindex = 0
    # boolean to check whether the graph was found 
	present = 0
    # set to store not found graphs
	notpresentset = set()
    
	while allindex < len(alldata):
        # initialize dataindex to track the set of found graphs 
		dataindex = 0
		while dataindex < len(data):
            # if graph was found 
			if data[dataindex] == alldata[allindex]:
				present = 1
			dataindex += 1
        # if graph was not found, insert in set 
		if present != 1:
			notpresentset.add(alldata[allindex])
        # reset boolean 
		present = 0
        # increment index of the set of all graphs 
		allindex += 1
	
	# open notpresentgraphs.txt to write
	file = open("notpresentquadgraphs.txt", "a")	
    	
    # for every item in notpresent set, store in notpresent.txt
	for x in notpresentset:
        	file.write(x + '\n')   
	file.close()

			
		
		
if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 3:
		print(f'Usage: python3 {sys.argv[0]} foundgraphs allgraphs', file=sys.stderr)
		sys.exit()
    # run comparegraphs on first and second argument
	comparegraphs(sys.argv[1], sys.argv[2])
	
