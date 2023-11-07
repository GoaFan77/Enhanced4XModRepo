
##Version 1.0 11-6-2023
##Changes the Max Refinery Count of neutral extractors.

import os, sys

NumRefineries = 6

def GetPath(): #gets the path of the current directory
  path = sys.argv[0]
  print(path)

  for i in range(-1,-100,-1):
    if path[i] == "\\":
      return path[0:i]
      break
    else:
      i = i-1

  print("Path not recognized/file name too long")
  quit

def writeEntity(fileName):
  
  infile = open(fileName, 'r')
  map = infile.read()
  map = map.split("\n")
  infile.close()
  
  if map[1] == 'entityType "Planet"':
    isNeutralAsteroid = False
    outfile = open(fileName, 'w')
    for i in map:
      if i == "":
        pass
      elif i.strip()[:33] == 'neutralMetalResourceAsteroidSetup' or i.strip()[:35] == 'neutralCrystalResourceAsteroidSetup':
        isNeutralAsteroid = True
        outfile.write(i + '\n')
      elif isNeutralAsteroid == True and i.strip()[:16] == 'maxRefineryCount':
        outfile.write('        maxRefineryCount ' + NumRefineries + '\n')
        isNeutralAsteroid = False
      else:
        outfile.write(i + '\n')
    
    print("Processed " + fileName)
    outfile.close()
    
  else:
    pass

def main():
  path = GetPath()
  listing = os.listdir(path)
  for infile in listing:
    if infile[-7:] == '.entity':
      writeEntity(infile)
                      
main()
