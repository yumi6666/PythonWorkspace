# -*- coding:utf-8 -*-

class TheThing(object):
    def __init__(self):
        self.number = 0
    
    def some_func(self):
        print "I got called."
    
    def add_me_up(self,more):
        self.number += more
        return self.number

        
#2 things instance

a = TheThing()
b = TheThing()

a.some_func()
b.some_func()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number        

# Pass a variable from one class to another
class TheMultiplier(object)
    def __init__(self, base):
        self.base = base
        
    def do_it(self, m):
        return m * slef.base

        
x = TheMultiplier(a.number)
print x.do_it(b.number)        


        
    
    
    
    
    
    
    
    
    