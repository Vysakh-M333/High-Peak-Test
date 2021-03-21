# -*- coding: utf-8 -*-
"""
Author-Vysakh M
Date-21/03/2021
Python 3

"""

infile = open("sample_input3.txt",'r')
lines = infile.readlines()
firstl = lines[0].split(":")
empno = int(firstl[len(firstl)-1])

#sorting the dictionary
goodies={}
for i in range(4,len(lines)):
    row = lines[i].split(":")
    goodies[row[0]] = int(row[1])
sortkey = sorted(goodies,key=goodies.get)
sortedgood = {}
for w in sortkey:
    sortedgood[w]=goodies[w]

#finding the minimum price
price = sorted(goodies.values())
mindiff = price[empno-1]-price[0]
index = 0
for i in range(0,len(price)-empno+1):
    diff = price[i+empno-1]-price[i]
    if(diff<mindiff):
        mindiff = diff
        index= i

#finding the minimum difference and writing into output file
d = price[index+empno-1]-price[index]
outfile = open("sample_output3.txt",'w')
outfile.write("The goodies selected for distribution are:\n")
outfile.write(" \n")
for i in range(index,index+empno):
    line = sortkey[i]+": "+str(sortedgood[sortkey[i]])+"\n"
    outfile.write(line)
line2 = "And the difference between the chosen goodie with highest price and the lowest price is "+str(d)
outfile.write(" \n")
outfile.write(line2)

infile.close()
outfile.close()