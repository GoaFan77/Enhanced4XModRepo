
##Version 1.0 11-16-12
##switches mesh files between Diplomacy and Rebellion .mesh format

import argparse

parser = argparse.ArgumentParser(description='Convets Sins mesh files between Rebellion and preRebellion formats.')
parser.add_argument('fileName', metavar='F', type=str,
                   help='file name of mesh file')
parser.add_argument('mode', metavar="T", type=str,
                   default="R", help="Which file structure to convert to. R = Rebellion, D = Diplomacy")

args = parser.parse_args()

infile = open(args.fileName, 'r')
mesh = infile.read()
infile.close()
mesh2 = ""

mesh = mesh.split("\n")
x = True
for i in mesh:
  if x and i != "TXT":
    quit
  else:
    x = False
    if i == "MeshData" and args.mode == "R":
      mesh2 += i + "\n"
      mesh2 += "\tmaxDiffuseMipLevel 0" + "\n"
    elif i == "\tmaxDiffuseMipLevel 0" and args.mode == "D":
      continue
    elif i != "":
      mesh2 += i + "\n";
    else:
      continue

outfile = open(args.fileName, 'w')
outfile.write(mesh2)
outfile.close()

