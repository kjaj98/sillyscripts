import numpy as np 
import matplotlib.pyplot as plt
from parser import XYZParser
from box import Box as b


coords = XYZParser('/Users/kitjoll/PHD/md_results/onetwofive_iron/fe_2_2000000steps/onehundredframes.xyz')
abc = 15.52125
centre_of_box = np.array([abc/2,abc/2,abc/2])
'''
with open('/Users/kitjoll/PHD/temp_data/iron_centre_box/output-ironcentred-nnp.xyz','w') as f:
    while coords.readNextFrame():
        f.write('376')
        f.write('\n')
        f.write('comment line baby'+' ')
        f.write('\n')
        coordy = coords.atoms
        iron_location = coordy[-1][1]
        for i in range(len(coordy)):
            atom_coords = coordy[i][1]
            atom_type = coordy[i][0]
            new_coord = np.subtract(atom_coords,iron_location)
            new_coord = np.add(new_coord,centre_of_box)
            #WRITE THE COORDS
            f.write(atom_type + ' ' + str(np.around(new_coord[0],5)) + ' ' + str(np.around(new_coord[1],5)) + ' ' + str(np.around(new_coord[2],5)) + '')
            f.write('\n')
'''
            
if True:
    #indicies_to_track =[135,136,137,
                        #12,13,14,
                        #195,196,197,
                        #306,307,308,
                        #219,220,221,
                        #156,157,158,375]
    oxy_indicies =[204,201,189,279,261,264]
    indicies_to_track = []
    for i in range(len(oxy_indicies)):
        indicies_to_track.append(oxy_indicies[i])
        indicies_to_track.append(oxy_indicies[i]+1)
        indicies_to_track.append(oxy_indicies[i]+2)
    indicies_to_track.append(375)
    
    
    with open('/Users/kitjoll/PHD/temp_data/output-octonlyfe2-onehundredframes.xyz','a') as f:
        while coords.readNextFrame():
            f.write(f'{len(indicies_to_track)}')
            f.write('\n')
            f.write('#comment line baby'+' ')
            f.write('\n')
            coordy = coords.atoms
            iron_location = coordy[-1][1]
            for i in range(len(coordy)):
                atom_coords = coordy[i][1]
                atom_type = coordy[i][0]
                new_coord = np.subtract(atom_coords,iron_location)
                new_coord = np.add(new_coord,centre_of_box)
                if i in indicies_to_track:
                    new_coord = ["{:0.4f}".format(v) for v in new_coord]
                    #WRITE THE COORDS
                    f.write(atom_type + ' ' + new_coord[0] + ' ' + new_coord[1] + ' ' + new_coord[2] + ' ')
                    f.write('\n')
                
    
    


