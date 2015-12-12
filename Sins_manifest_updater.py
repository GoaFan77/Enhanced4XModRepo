##Sins Manifest Updater By GoaFan77
##Version 1.0 2-2-12

import os, sys

def GetPath(): #gets the path of the current directory
  path = sys.argv[0]
  print(path)

  for i in range(-1, -100, -1):
    if path[i] == "\\":
      return path[0:i]
      break
    else:
      i = i-1

  print("Path not recognized/file name too long")
  quit

def ReadManifest(): #reads the manifest.entity file of the current directory
  infile = open('entity.manifest', 'r')
  infile.readline()
  num = infile.readline()
  num = num.split()
  num = int(num[1])
  manifest = infile.read()
  manifest = manifest.rstrip('\n')
  infile.close()

  infile = open('entity.manifest', 'r')
  infile.readline()
  infile.readline()
  
  entitylist = {}
  for i in range (2, num+2):
    line = infile.readline()
    line = line.rstrip('\n')
    line = line[11:]
    line = line.lstrip('"')
    line = line.rstrip('"')
    entitylist[line] = True

  infile.close()
  return num, entitylist, manifest

def CopyManifest():
    infile = open('entity.manifest', 'r')
    outfile = open ("Oldentity.manifest", 'w')
    file = infile.read()
    infile.close()
    outfile.write(file)
    outfile.close()

def main():
  CopyManifest()
  path = GetPath()
  path = path + "/GameInfo"
  num, entityList, manifest = ReadManifest()
  newEntities = []
  listing = os.listdir(path)
  for infile in listing:
    if infile[-7:] == '.entity':
      if not infile in entityList:
        print(infile)
        newEntities.append(infile)

  for i in newEntities:
    manifest = manifest + '\nentityName "' + i + '"'
    num += 1

  manifest = "TXT\nentityNameCount " + str(num) +'\n'+ manifest + "\n"

  outfile = open ("entity.manifest", 'w')
  outfile.write(manifest)
  outfile.close()
  
main()
