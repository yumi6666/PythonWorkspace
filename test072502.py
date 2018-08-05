# -*- coding:utf-8 -*-
import functools

#decorator log
def log_dec(f):
    @functools.wraps(f)
    def wrapper(*args , **kwargs):
        print 'call %s()' %f.__name__
        return f(*args , **kwargs)
    print 'wrapper name = %s' % wrapper.__name__    
    return wrapper
    
@log_dec
def f1(x):
    print 'f1 func ran!'

sorted_ignore_case = functools.partial(sorted, cmp = lambda s1, s2: cmp(s1.upper(),s2.upper()))
    
    
if __name__ == '__main__':
    print f1(10)
    words = ['boring','Zoo','abandon','none','title']
    print sorted_ignore_case(words)