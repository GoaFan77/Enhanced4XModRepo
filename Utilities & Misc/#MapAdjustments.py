##Sins MapAdjustments By GoaFan77
##Version 1.1 12-28-18

import os, sys

artifactChance = 0.350000
bonusChance = 0.800000
skipLines = ["isRaidingPlayer", "isInsurgentPlayer", "isOccupationPlayer", "isMadVasariPlayer"]
mapVersion = 193

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
    if not any("dlcID" in line for line in map):
        map[-1] = "dlcID 204880"
        map.append('\n')
    
    for i in map:
        if not i.isspace() and i != '\n' and i != "":#i.replace('/t', "") != "" and i.replace('/t', "") != "\n":
            lineName, lineValue = i.split()[0], i.split()[1]
            if lineName == 'planetArtifactDensity' and lineValue > 0:
                i = "planetArtifactDensity " + str(artifactChance)
            elif lineName == 'planetBonusDensity' and lineValue > 0:
                i = "planetBonusDensity " + str(bonusChance)
            elif lineName == "versionNumber":
                i = "versionNumber " + str(mapVersion)
            elif lineName == "isNormalPlayer":
                i = '\t' + 'playerType "Normal"' 
            # Don't output obsolete lines.  
            elif lineName in skipLines:
                continue            
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
