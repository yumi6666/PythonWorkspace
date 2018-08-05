# -*- coding:utf-8 -*-


def _dec_log(f):
    def fn(x):
        print 'call' + f.__name__ +'()'
        return f(x)
    return fn


@_dec_log
def f1(x):
    return x*x*x
    

@_dec_log
def f2(x):
    return x*x
  
if __name__ == '__main__':
    f1 = _dec_log(f1)
    print f1(6)