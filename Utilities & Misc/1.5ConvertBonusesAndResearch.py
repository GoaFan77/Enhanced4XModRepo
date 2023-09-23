
##Version 1.0 6-9-13
##Updates planet bonuses and research for Sins Rebellion 1.5

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

def writeEntity(fileName):
  
  infile = open(fileName, 'r')
  map = infile.read()
  map = map.split("\n")
  infile.close()
  
  if map[1] == 'entityType "PlanetBonus"':
    outfile = open(fileName, 'w')
    for i in range(len(map)):
      if map[i] == "":
        pass
      elif i == 12:
        outfile.write(map[i] + '\n')
        tabCount = map[i].count('\t')
        outfile.write('\t' * tabCount + 'floatBonus:BombingDamageAsDamageTargetAdjustment 0.000000' + '\n')
        outfile.write('\t' * tabCount + 'floatBonus:MaxAllegiancePercBonus 0.000000' + '\n')
      elif i == 20:
        outfile.write(map[i] + '\n')
        tabCount = map[i].count('\t')
        outfile.write('\t' * tabCount + 'floatBonus:ShipBuildCostAdjustment 0.000000' + '\n')
        outfile.write('\t' * tabCount + 'floatBonus:WeaponDamageAtGravityWellMultiplier 0.000000' + '\n')
        outfile.write('\t' * tabCount + 'intBonus:MaxSpaceMines 0' + '\n')
        outfile.write('\t' * tabCount + 'intBonus:MaxStarbases 0' + '\n')
      elif i == 22:
        outfile.write(map[i] + '\n')
        tabCount = map[i].count('\t')
        outfile.write('\t' * tabCount + 'dlcId 204880' + '\n')
      else:
        outfile.write(map[i] + '\n')
    
    outfile.close()

    
  elif map[1] == 'entityType "ResearchSubject"':
    outfile = open(fileName, 'w')
    for i in map:
      if i == "":
        pass
      elif i.strip()[:18] == 'uniqueOverlayBrush':
        outfile.write(i + '\n')
        tabCount = i.count('\t')
        outfile.write('\t' * tabCount + 'dlcId 204880' + '\n')
      else:
        outfile.write(i + '\n')
    
    outfile.close()
    
  else:
    pass

def main():
  path = GetPath()
  listing = os.listdir(path)
  for infile in listing:
    if infile[-7:] == '.entity':
      print infile
      writeEntity(infile)
                      
main()
