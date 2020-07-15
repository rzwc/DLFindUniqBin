# Program used to compare the output between Linux strings and stringlish and store the "bad" output in text file

import sys

# Linux strings program written in python
import strings

# Stringlish program
import stringlish 

# class used to receive output of strings and add to stringsset
class StringInsert:

    # initialize value of string to the empty string
    def __init__(self, string = ""):
        self.string = string

    # buffer output of characters until "\n" is reached so entire string is inserted into the set
    def write(self, s):                                                                                                                                            
        
        # add character to empty string
        if s != '\n':
            
            self.string += s
            
        # reach new line, insert string into set
        # reset empty string 
        elif s == '\n':
        
            stringsset.add(self.string)
            self.string = ''      
    
    #
    def flush(self):
        pass

# class used to receive output of stringlish and add to stringlishset
class StringlishInsert:

    # initialize value of string to the empty string
    def __init__(self, string = ""):
        self.string = string

    # buffer output of characters until "\n" is reached so entire string is inserted into the set
    def write(self, s):

        # add character to empty string        
        if s != '\n':
            
            self.string += s
            
        # reach new line, insert string into set
        # reset empty string 
        elif s == '\n':
            stringlishset.add(self.string)
            self.string = ''      

    #
    def flush(self):
        pass

if __name__ == '__main__':

    # printing correct usage if number of arguments is not valid
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
        sys.exit()
        
    # open file for stringlish
    for file in sys.argv[1:]:
        try:
            # open binary file to read 
            f = open(file, 'rb')
            s = f.read()
            f.close()
        except IOError as e:
            # IO Error message
            sys.stderr.write('%s: %s\n' % (file, e.strerror))
            continue

    # remember initial output file object
    old_output = sys.stdout
    
    # new output for strings output
    insert = StringInsert()
    
    # set output to new output 
    sys.stdout = insert
    
    # create set for strings output
    stringsset = set()
    
    # run strings on binary file
    strings.strings(sys.argv[1])
    
    # new output for stringlish output
    insert = StringlishInsert()
    
    # set output to new output
    sys.stdout = insert
    
    # create set for stringlish output
    stringlishset = set()
    
    # run stringlish on binary file 
    stringlish.newfile(file)  
    stringlish.filter_printable(s)  
    
    # set output back to original output
    sys.stdout = old_output
            
    # compare two sets by finding the difference between them and storing them in the set diff
    diff = stringsset.difference(stringlishset)
    
    # open diff.txt to write
    file = open("diff.txt", "a")
    
    # for every item in diff set, store in diff.txt
    for x in diff:
    
        file.write(x + '\n')  
        
    file.close()
