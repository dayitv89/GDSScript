from spellCheck import *

while(True):
    w = raw_input('enter word: ').split()
    print ' '.join([correct(x) for x in w])
