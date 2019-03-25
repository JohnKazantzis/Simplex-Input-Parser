#!/usr/bin/env python3
#coding: utf-8
import re
import sys

def inputCheck(fileLines):
    numOfVars = 0
    numOfSigns = 0
    invalidInput = False

    #Checking if there is mix or max before z
    minMaxCheck = re.search("(\A(\s)*max\s)|(\A(\s)*min\s)",fileLines[0])

    if(minMaxCheck == None):
        print("Invalid input!")
        invalidInput = True

    #Checking if there is st,s.t. or subject to before the first constrain
    stCheck = re.search("\A(\s)*st\s|\A(\s)*s.t.\s|\A(\s)*subject to\s",fileLines[1])
    if(stCheck == None):
        print("Invalid input!")
        invalidInput = True

    #(z) -> Checking if all the variables have signs
    subLine = re.sub("\A\s*min|max","",fileLines[0])

    zSignCheck = re.findall("([a-zA-Z]\d\d*)",subLine)
    numOfVars = numOfVars + len(zSignCheck)

    zSignCheck = re.findall("[+-]",subLine)
    numOfSigns = numOfSigns + len(zSignCheck)

    zSignCheck = re.search("(\A\s*[+-]\d*[a-zA-Z])",subLine)
    if zSignCheck == None:
        numOfSigns = numOfSigns + 1

    if numOfVars != numOfSigns:
        print("Invalid input!")
        invalidInput = True

    #(Constrains) -> Checking if all the variables have signs
    #Same as the z sign check
    #The z signs could have been checked with the constrain signs
    #inside the for loop
    for x in range(1,len(fileLines)-1):
        constrainSignCheck = re.findall("([a-zA-Z]\d\d*)",fileLines[x])
        numOfVars = numOfVars + len(constrainSignCheck)

        constrainSignCheck = re.findall("[+-]",fileLines[x])
        numOfSigns = numOfSigns + len(constrainSignCheck)

        if x==1:
            fileLines[x] = re.sub("\A\s*st|s.t.|subject\sto","",fileLines[x])

        constrainSignCheck = re.search("(\A\s*[+-]\d*[a-zA-Z])",fileLines[x])
        if constrainSignCheck == None:
            numOfSigns = numOfSigns + 1

    if numOfVars != numOfSigns:
        print("Invalid input!")
        invalidInput = True

    #(Constrains) -> Checking if the (≤, =, ≥) and bi exist
    for x in range(1,len(fileLines)-1):
        compSignCheck = re.search("([≤≥=]\s*\d\s*\Z)|([≤≥=]\s*\d\s*\n)",fileLines[x])
        if compSignCheck == None:
            print("Invalid input!")
            invalidInput = True

def main():
    fileLines = []

    if len(sys.argv) != 2:
        print("Use python3 ex1.py -h or python3 ex2.py --help")
        print("to learn how run the script")
        exit(0)

    if sys.argv[1]== "-h" or sys.argv[1]== "--help":
        print("Usage: python3 ex1.py [Input File Name]")
        exit(0)

    #Opening text file
    input_obj = open(sys.argv[1],"r")
    input = input_obj.read()

    #Splitting the string's lines
    for line in input.splitlines():
        fileLines.append(line)

    #Calling the fuction responsible for checking the input
    inputCheck(fileLines)

    print("Ok!")

if __name__ == '__main__':
    main()
