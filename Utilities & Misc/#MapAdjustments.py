##Sins MapAdjustments By GoaFan77
##Version 1.0 6-23-12

import os, sys

artifactChance = 0.350000
bonusChance = 0.800000

def GetPath(): #gets the path of the current directory
  path = sys.argv[0]
  print (path)

  for i in range(-1,-100,-1):
    if path[i] == "\\":
      return path[0:i]
      break
    else:
      i = i-1

  print ("Path not recognized/file name too long")
  quit

def writeGalaxy(fileName): #reads the manifest.entity file of the current directory
  infile = open(fileName, 'r')
  map = infile.read()
  infile.close()

  outfile = open(fileName, 'w')
  map = map.split("\n")
  for i in map:
    if not i.isspace() and i != '\n' and i != "":#i.replace('/t', "") != "" and i.replace('/t', "") != "\n":
      if i.split()[0] == 'planetArtifactDensity':
        i = "planetArtifactDensity " + str(artifactChance)
      elif i.split()[0] == 'planetBonusDensity':
        i = "planetBonusDensity " + str(bonusChance)
      outfile.write(i + '\n')
  outfile.close()

def main():
  path = GetPath()
  listing = os.listdir(path)
  for infile in listing:
    if infile[-7:] == '.galaxy':
      print(infile)
      writeGalaxy(infile)
  
main()
