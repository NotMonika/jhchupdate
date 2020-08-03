import _jhch_func as _jf
import sys
import os
import atexit
log=open('jhch_log.log')
helpfp=open('help.txt')
def delstrend(s):
	j=''
	for i in s:
		if not i==s[-1]:
			j+=i
	return j
if __name__=="__main__":
    if len(sys.argv)>1:
        if sys.argv[1]!="-h":
            path=os.path.abspath(sys.argv[1])
            file=open(path)
            codes=file.readlines()
            print('open:',path)
            for i in codes:
                i=_jf.macrot(delstrend(i))
                split1=i.split(' ',1)
                split1+=['0']
                split2=split1[1].split(',')
                _jf.exec(eval('_jf.'+split1[0]),*split2)
            
        else:
            print(helpfp.read())
    else:
        print('''jhch1.0 shell''')
        while True:
                try:
                        str1=_jf.macrot(input('>>>'))
                        split1=str1.split(' ',1)
                        split1+=['0']
                        split2=split1[1].split(',')
                        _jf.exec(eval('_jf.'+split1[0]),*split2)
                except Exception as e:
                        print(e)

            
