
##Version 1.0 6-23-12
##Adds level 3, medium affects and new research prereq options

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

def writeEntity(fileName): #reads the manifest.entity file of the current directory
  infile = open(fileName, 'r')
  map = infile.read()
  infile.close()

  outfile = open(fileName, 'w')
  map = map.split("\n")
  x = "x"
  for i in map:
    if i == "":
      continue
    if  i != "" and i != '\n' and i.isspace() == False:
      if x.strip().split()[0] == "Level:2" and i.strip().split()[0] != "Level:3":
        tabCount = x.count('\t')
        outfile.write('\t' * tabCount + "Level:3 " + x.strip().split()[1] + '\n')
      elif x.strip().split()[0] == "smallEffectName" and i.strip().split()[0] == "largeEffectName":
        tabCount = x.count('\t')
        outfile.write('\t' * tabCount + "mediumEffectName " + i.strip().split()[1] + '\n')
      elif x.strip() == "NumResearchPrerequisites 0" and i.strip().split()[0] != "RequiredFactionNameID":
        tabCount = x.count('\t')
        outfile.write('\t' * tabCount + "RequiredFactionNameID \"\"\n")
        outfile.write('\t' * tabCount + "RequiredCompletedResearchSubjects 0\n")
      elif x.strip().split()[0] == "Level" and i.strip().split()[0] != "RequiredFactionNameID":
        tabCount = x.count('\t') - 1         
        outfile.write('\t' * tabCount + "RequiredFactionNameID \"\"\n")
        outfile.write('\t' * tabCount + "RequiredCompletedResearchSubjects 0\n")
      elif x.strip().split()[0] == "burstDelay" and i.strip().split()[0] != "muzzleEffectName":
        tabCount = x.count('\t')
        outfile.write('\t' * tabCount + "fireDelay 0.000000\n")
        
      outfile.write(i + '\n')
      
    if i == "" and x.strip().split()[0] == "Level:2":
       tabCount = x.count('\t')
       outfile.write('\t' * tabCount + "Level:3 " + x.strip().split()[1] + '\n')
       
    x = i
    
  outfile.close()

def main():
  path = GetPath()
  listing = os.listdir(path)
  for infile in listing:
    if infile[-7:] == '.entity':
      print infile
      writeEntity(infile)
                      
main()
