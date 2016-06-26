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
  theFile = open("#SoundDialogFormatter.txt", 'w')
  num = 0
  for infile in listing:
    if infile.startswith("Dialog_ING"):
      theFile.write('effect\n\tname "' + infile.strip(".ogg") + '"\n\tfileName "' + infile + '"\n')
      num += 1
  theFile.close()
  print("Number of lines: " + str(num))
  
main()
