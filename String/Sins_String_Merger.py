##Sins Manifest Updater By GoaFan77
##Version 1.0 2-2-12

import os, sys

def GetPath(): #gets the path of the current directory
  path = sys.argv[0]
  print path

  for i in range(-1,-100,-1):
    if path[i] == "\\":
      return path[0:i]
      break
    else:
      i = i-1

  print "Path not recognized/file name too long"
  quit

def ReadStringAdditions(): #reads the string additions file of the current directory
  count = 0
  line = "x"
  infile = open('String Additions.txt', 'r')
  
  while line != '':
    line = infile.readline()
    line = line.rstrip('\n')
    if line == "StringInfo":
      count += 1

  infile.close()
  infile = open('String Additions.txt', 'r')
  newStrings = infile.read()

  return count, newStrings

def ReadString():
  strings = ""
  infile = open('English Source.str', 'r')
  infile.readline()
  line = infile.readline()
  line = line.split()
  num = int(line[1].rstrip('/n'))
  while line != "":
    line = infile.readline()
    strings += line

  infile.close()
  return num, strings

def WriteString(string1, string2, count): #writes the final string
  outfile = open('English.str', 'w')
  outfile.write('TXT\n')
  outfile.write('NumStrings ' + str(count) + '\n')
  outfile.write(string1)
  outfile.write(string2)
  outfile.close()
  
def main():
  num, newStrings = ReadStringAdditions()
  newStrings += '\n'
  num2, strings = ReadString()
  num += num2
  WriteString(newStrings, strings, num)
  print "Complete"
  
  
main()
