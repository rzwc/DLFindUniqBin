import sys
import strings2
import stringlish 

class StringInsert:

    def __init__(self, string = ""):
        self.string = string

    def write(self, s):                                                                                                                                            
        
        if s != '\n':
            
            self.string += s
            
        elif s == '\n':
        
            stringsset.add(self.string)
            self.string = ''      

    def flush(self):
        pass

class StringlishInsert:

    def __init__(self, string = ""):
    
        self.string = string

    def write(self, s):
        
        if s != '\n':
            
            self.string += s
        elif s == '\n':
            stringlishset.add(self.string)
            self.string = ''      

    def flush(self):
        pass

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} filename', file=sys.stderr)
        sys.exit()
        
    for file in sys.argv[1:]:
        try:
            f = open(file, 'rb')
            s = f.read()
            f.close()
        except IOError as e:
            sys.stderr.write('%s: %s\n' % (file, e.strerror))
            continue

    
    old_output = sys.stdout
    
    insert = StringInsert()
    
    sys.stdout = insert
    
    stringsset = set()
    
    strings2.strings(sys.argv[1])
    
    insert = StringlishInsert()
    
    sys.stdout = insert
    
    stringlishset = set()
    
    stringlish.newfile(file)   

    stringlish.filter_printable(s)  
    
    sys.stdout = old_output
    
    print(len(stringsset))
            
    diff = stringsset.difference(stringlishset)
    
    file = open("diff.txt", "w")
    
    for x in diff:
        file.write(x + '\n')
        
    file.close()
