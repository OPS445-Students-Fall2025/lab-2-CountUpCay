#!/usr/bin/env python3

# Name: Cayson Jack
# Authur ID: cjack4
# Date: 09/19/2025

import sys            #Allows for the use of sys.argv

if len(sys.argv) != 3:    #Checks to see if there are correct amount of arguments
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ", you are " + str(age) + " years old.")
