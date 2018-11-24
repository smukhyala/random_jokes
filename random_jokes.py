#!/usr/bin/env python

import random
import os.path
import sys
import getopt

####################################################################
def help():
    sys.exit('python random_jokes_edited.py -d <jokes_database.txt>')

# Random in Python
def random_line(afile,count):
    rnumber = random.randint(0,count-2)
    for num, aline in enumerate(afile, 0):
        if(num == rnumber and num % 2 == 0):
            nline = next(afile)
            return aline + nline
        elif(num == rnumber):
            aline = next(afile)
            nline = next(afile)
            return aline + nline
        else:
            continue
####################################################################
def line_count(db_name):
    count= -1
    if(os.path.isfile(db_name)):
        count = len(open(db_name).readlines())
    else:
        sys.exit('Sorry. Your file does not exist.')
    return(count)
####################################################################
#main###############################################################
try:
    options, args = getopt.getopt(sys.argv[1:], "d:")
except getopt.GetoptError as err:
    help()

default_jokes = 'jokes_database.txt'
db_name = default_jokes

if(len(options)):
    for opt, arg in options:
        if opt in ['-d']:
            db_name = arg
        else:
            help()
elif len(args) == 1:
    db_name = args[0]
else:
    help()

print("I will attempt to read this file: " + db_name)

fcount = line_count(db_name)
sj = open(db_name, "r")
joke = random_line(sj,fcount)
print(joke)
####################################################################
