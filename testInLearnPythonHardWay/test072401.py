# -*- coding:utf-8 -*-

class Animal(object):
##  TODO:
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    
    def __init__(self, name):
        self.name = name
    ##set pet
        self.pet = None
        
class Employee(Person):
    
    def __init__(self, name, salary):
        ##继承person类的属性
        super(Employee, self).__init__(name)
        self.salary = salary
        
    
    
