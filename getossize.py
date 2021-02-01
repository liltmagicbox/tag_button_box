import os
from os.path import join, getsize

def getdirsize(di):
    sss=0
    for root, dirs, files in os.walk(di):
        #result = "%s : %.f MB in %d files." % (os.path.abspath(root), sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0), len(files))
        #print(result)
        ss=sum([getsize(join(root, name)) for name in files]) // (1024.0 * 1024.0)
        #print(ss)
        sss+=ss
    return "{}MB".format(sss)

if __name__=="__main__":
    di = input('targetdir?')
    print( getdirsize(di) )
