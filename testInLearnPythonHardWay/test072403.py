# -*- coding:utf-8 -*-

#demo implicit inheritance

class Parent_class_1(object):
    def __init__(self):
        self.name = "P1"
    def implicit(self):
        print "PARENT_CLASS implicit()"
        
class Child_class_1(Parent_class_1):
    pass

p1 = Parent_class_1()
c1 = Child_class_1()

p1.implicit()
c1.implicit()

class Parent_class_2(object):
    def __init__(self):
        self.name = "p2"
    def override_func(self):
        print "Parent_class_2 override_func."
        
class Child_class_2(Parent_class_2):
    def override_func(self):
        print "Child_class_2 override_func."
        
p2 = Parent_class_2()
c2 = Child_class_2()

p2.override_func()
c2.override_func()

class Parent_class_3(object):
    def __init__(self):
        self.name = "p3"
    def altered(self):
        print "Parent_class_3 altered()"
        
class Child_class_3(Parent_class_3):
    def altered(self):
        print "Child_class_3, BEFORE parent altered()"
        super(Child_class_3, self).altered()
        print "Child_class_3, AFTER parent altered()"
        super(Child_class_3, self).altered()
        
p3 = Parent_class_3()
c3 = Child_class_3()

p3.altered()
c3.altered()
    








