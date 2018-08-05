from sys import argv
from os.path import exists

script , from_file  , to_file = argv

print "Copying form %s to %s" %(from_file , to_file)

in_file = open(from_file)
#indata = in_file.read()
indata = in_file.read()

print "The input file is %d byte" % len(indata)
print "The input lines = %s" %indata

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')

if exists(to_file):
    print "Now try to truncate the output file."
    out_file.truncate();

out_file.write(indata)

print "All done."

out_file.close()
in_file.close()



def mkdir(path):
    import os
    
    path = path.strip()
    path = path.rstrip("\\")
    
    isExists = os.path.exists(path)
    
    if not isExists:
        os.makedirs(path)
        
        print path+"makedir succeed!"
        return True
    
    else:
        print path+"already exists!"
        return False
    
    
