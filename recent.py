#!/usr/bin/python

import sys
import os
import time

def usage():
    print "usage : recent.py [filename]"

if len(sys.argv) == 1:
    usage()
    sys.exit(1)


### MAIN ####

recent_files= os.path.join(os.environ["HOME"],'.vim/recent_files')

filename=sys.argv[1]
date=time.strftime('%Y%m%d %H:%M' ,time.localtime())
append=True

if os.path.exists(recent_files):
    fic=open( recent_files, 'r' )
    for line  in fic.readlines():
        if line[:-19] == filename:
            append=False
            break
   
fic.close()

if append:
    fic=open( recent_files, 'a' )
    print >> fic,filename + "    " + date
    fic.close()
