import time as t
import os
import sys


class base:

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
   
   
    def tprint(text, delay=0.05):
        base.text = text
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            t.sleep(delay)
    print()

    def tprinty(pretext, text, delay=0.05):
        base.pretext = text
        base.text = text
        for char in text:
            for i in range(8):
                sys.stdout.write(char)
                sys.stdout.flush()
                t.sleep(delay)
        print()

    
    def loading():
        base.tprinty("Loading","...")


class Elm:
    def __init__(self, atomicnumber, element):
        self.atomicnumber = atomicnumber
        self.element = element


    def intcheck(input):
        base = int(input)
        properint = list(range(1,119))
        if base in properint:
            inlist = "True"
            return
        else:
            inlist = "False"
        base.loading()
        