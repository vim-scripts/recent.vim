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

filename=sys.argv[1]
tmpfilename=os.path.join(os.environ["HOME"],'.vim/.recent_files.tmp')
recent_files= os.path.join(os.environ["HOME"],'.vim/recent_files')
date=time.strftime('%Y%m%d %H:%M' ,time.localtime())

tmpfile=open(tmpfilename, "a")

if os.path.exists(recent_files):
    fic=open(recent_files, 'r')
    for line in fic.readlines():
        if line[:-19] != filename:
            print >> tmpfile, line[:-1]

    fic.close()

print >> tmpfile,filename + "    " + date
tmpfile.close()

os.rename(tmpfilename, recent_files)
