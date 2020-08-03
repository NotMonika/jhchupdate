'''jhch'''

import time as time
import sys as sys
import os as os
import re
sys.path+=[os.path.abspath("jhchlib")]
try:
    import julia
    j=julia.Julia()
except:
    julia=None
class Func:
    def __init__(self,name,ffp):
        self.name=str(name)
        self.ffp=ffp
    def __repr__(self):
        return f'<Jhch Func \'{self.name}\' object from python func \'{self.ffp.__name__}\'>'
    __str__=__repr__
macros={}
echo=Func('echo',print)
sleep=Func('sleep',(lambda i:time.sleep(int(i))))
_exit=exit=Func('exit',quit)
system=Func('',os.system)
pimport=Func('pimport',(lambda name:globals().update({name:__import__(name)})))
macro=Func('',lambda name,str1:macros.update({name:str1}))

def exec(func,*args):
    '''the jhch run from exec.'''
    func.ffp(*args)
def macrot(str_):
    for i,j in macros.items():
        str_=str_.replace('@'+i+'@',j)
    return str_
