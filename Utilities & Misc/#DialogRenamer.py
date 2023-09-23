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

def main():
  path = GetPath()
  listing = os.listdir(path)
  for infile in listing:
    if infile.startswith("Dialog ING"):
      os.rename(infile, infile.replace(" ", "_"))
  
main()
