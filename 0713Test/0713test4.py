import pdb

def count():
    fs = []
    for i in range(1,4):
        def f():
            print "f()"i
            return i*i
        fs.append(f)
    return fs
    
f1,f2,f3 = count()

print f1()