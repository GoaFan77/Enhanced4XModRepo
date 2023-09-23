##Version 1.0 3-31-19
##Moves points in a Sins mesh file by a given x/y/z value.

from decimal import Decimal, getcontext

getcontext().prec = 12 

def updateMeshpoints(fileName, xAdjust, yAdjust, zAdjust):
  
    # Open the file and build a string array of lines.
    with open(fileName, 'r') as infile:
        map = infile.read()
        map = map.split("\n")
        
    # Check for the end of the points section so no other section of the file is modified.
    done = False
  
    with open(fileName, 'w') as outfile:
        for i in range(len(map)):
            if 'NumVertices' in map[i]:
                # This line marks the end of the point section
                done = True
                outfile.write(map[i] + '\n')
                pass
            elif not done and 'Position' in map[i]:
                # Slice out the coordinates and rebuild the Position line with the adjustments.
                coordinates = map[i][map[i].find('[') + 1:map[i].find(']')]
                coordinates = coordinates.split()
                coordinates[0] = Decimal(coordinates[0]) + xAdjust;
                coordinates[1] = Decimal(coordinates[1]) + yAdjust;
                coordinates[2] = Decimal(coordinates[2]) + zAdjust;
                tabCount = map[i].count('\t')
                newPoistion = '\t' * tabCount + 'Position [ ' + str(coordinates[0]) + ' ' + str(coordinates[1]) + ' ' +  str(coordinates[2]) + ' ]' + '\n'
                outfile.write(newPoistion)
                # print(newPoistion)
            else:
                outfile.write(map[i] + '\n')
                
    return done         

def main():
    updateMeshpoints('filename.mesh', Decimal(0), Decimal(0), Decimal(42.78))
                      
main()
