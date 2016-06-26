##Sins Manifest Updater By GoaFan77
##Version 1.0 2-2-12

import os, sys, shutil

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

def writeEntity(fileName):
  infile = open(fileName, 'r')
  map = infile.read()
  infile.close()

  outfile = open(fileName, 'w')
  map = map.split("\n")
  x = "x"
  for i in map:
    if i == "":
      continue
    elif  i[0:14] == "ShieldMeshName" and i.find('""') == -1:
      outfile.write('ShieldMeshName "' + i[i.find('"') + 1:i.rfind('"')]+ 'shield"\n')
    else:    
      outfile.write(i + '\n')
      
##    if i == "" and x.strip().split()[0] == "Level:2":
##       tabCount = x.count('\t')
##       outfile.write('\t' * tabCount + "Level:3 " + x.strip().split()[1] + '\n')
##       
##    x = i
    
  outfile.close()

def main():
  path = GetPath()
  listing = os.listdir(path)
  for infile in listing:
    if (infile[-7:] == ".entity"):
      writeEntity(infile)
  
main()
