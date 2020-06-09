# Program imitating Linux strings command
import sys

# minimum length of string
MINLEN = 4

# is printable strings function, takes character
# returns true if integer representing Unicode character is between ' ' and - 
# or is tab character
def isprint(b):
	return b >= ord(' ') and b <= ord('~') or b == ord('\t')

# output printable strings 
def strings(filename):
	try:
        # open binary file to read
		f = open(filename, 'rb')
		data = f.read()
    # print usage format if IOError
	except IOError as e:
		print(f'{filename}: {e.strerror}', file=sys.stderr)
		sys.exit()
	
    # initialize variable to track index, and the last character of the string if found 
	index = 0
	last = 0
    
    # keep loop inside length of data
    # if string is found past len(data) - MINLEN, string will be less than 4 characters
	while index < len(data) - MINLEN: 
        # set last character checked as current index 
		last = index
        
        # if current indexed character is a printable character 
		if isprint(data[index]) == True:
            # start index is the current index, track head of the string
			start = index
            # counter to count to MINLEN 
			counter = 0
            # boolean to ascertain whether string is printable or not 
			canprint = 0
            # number of printable characters in 4 characters
			length = 0
            
            # loop through minimum length to check whether there are 4 consecutive printable characters 
			while counter < MINLEN:
                # if current indexed character is printable, increase length by 1
				if isprint(data[index]) == True:
					length += 1
                # move to next character
				index += 1
                #increase counter
				counter += 1
            
            # if there are 4 consecutive printable characters, canprint is true
			if length == MINLEN:
				canprint = 1
			
            # set index back to head of the string 
			index = start
			
            # while string is printable 
			while canprint == 1:
                # print Unicode character of the index, space each character with no space 
				print(chr(data[index]), end = "")
                # check if next index is a printable character 
				if isprint(data[index+1]) == False:
                    # set the last index checked as current index 
					last = index 
                    # set canprint boolean to not printable
					canprint = 0
                    # print new line 
					print()
                #increment index 
				index += 1
        # new index is the last index checked + 1
		index = last + 1
	f.close()
	
if __name__ == '__main__':
    # usage format
	if len(sys.argv) != 2:
		print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
		sys.exit()
    # run strings on first argument
	strings(sys.argv[1])