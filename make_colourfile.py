import numpy as np 
from parser import XYZParser

coords = XYZParser('/Users/kitjoll/PHD/nnp/fe3_nnp/nnp_md_retrain/fifth/fine_grain_crashed/md3/trying_md-nnp-forces-std-1.xyz')

forces = []
frame = 0
#calc avg force for each atom for each frame store in list of lists 
while coords.readNextFrame():
    #check the index of the frames
    if frame%1000 == 0:
        print(f'Processing frame {frame}')
    forces_frame = []
    for i in range(len(coords.atoms)):
        avg_force_on_atom = abs((coords.atoms[i][1][0]+coords.atoms[i][1][1]+coords.atoms[i][1][2])*1/3)
        forces_frame.append(avg_force_on_atom)
    forces.append(forces_frame)
    frame +=1

#now write colourfile 
'''

The file containing the colors needs to have a single line per frame and
then a single number per atom defining the color of that atom. THe color
scale can be changed, e.g. that the largest value is blue and the lowest
value is red, while all values in between are scaled in between blue/red.

'''

with open('colorfile','w') as f:       
    for i in range(len(forces)):
        for j in range(len(forces[0])):
            f.write(str(forces[i][j])+' ')
        f.write('\n')
print('finished')
