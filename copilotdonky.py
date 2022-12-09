import numpy as np 

# mr copilot, take the wheel
# please write me a function to do the following
# import the data file frame by frame using xyz parser
# make a histograme out of the distances between all pairs of atoms in every frame

# the data file is in the same directory as this file
pathy = '/Users/kitjoll/PHD/nnp/fe3_nnp/nnp_md_retrain/fifth/finished_runs/positions/positions/positions5.xyz'

from parser import XYZParser
from box import Box as b

coords = XYZParser(pathy)

track=0
box = b(cellfn = '/Users/kitjoll/PHD/Philipp_DFT_ML/python/nnp-md/cell.inc')

while coords.readNextFrame():
    if track%10 == 0:
        print(track)
    if track == 1000: 
        break
    data = coords.atoms
    #extract the elements and then loop over pairs of elements to get the distances
    elements = [data[i][0] for i in range(len(data))]
    pairs_of_elements = [(elements[i], elements[j]) for i in range(len(elements)) for j in range(i+1, len(elements))]
    pairs_of_distances = []
    dict1 = {
        'OO':[],
        'OH':[],
        'OFe':[],
        'HH':[],
        'HFe':[],
        'FeFe':[]
        }
    # alternative method
    # loop over data twice in a nested loop
    # get the distance between the two atoms and label the pair of atoms by the pair of elements
    # store the distance in a dictionary labelled by the pair of elements
    # then only need to loop over data twice per frame

    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                coord1 = data[i][1]
                coord2 = data[j][1]
                v = np.subtract(coord1,coord2)
                vector = box.pbc(v)
                wrapped = np.linalg.norm(vector)
                atom1type = data[i][0]
                atom2type = data[j][0]
                if atom1type=='O' and atom2type=='O':
                    dict1['OO'].append(wrapped)
                elif atom1type=='O' and atom2type=='H' or atom1type=='H' and atom2type=='O':
                    dict1['OH'].append(wrapped)
                elif atom1type=='O' and atom2type=='Fe' or atom1type =='Fe' and atom2type =='O':
                    dict1['OFe'].append(wrapped)
                elif atom1type=='H' and atom2type=='H':
                    dict1['HH'].append(wrapped)
                elif atom1type== 'H ' and atom2type=='Fe' or atom1type=='Fe' and atom2type=='H':
                    dict1['HFe'].append(wrapped)
                elif atom1type=='Fe' and atom2type=='Fe':
                    dict1['FeFe'].append(wrapped)     
    track+=1
    
# now loop over the dictionary and make a histogram for each pair of elements
# make a function that takes the dictionary and makes a histogram for each pair of elements
rmax = 6
dr = 0.1
rspace = np.linspace(0,rmax,int(rmax/dr))
dict2 = {
        'OO':np.zeros(len(rspace)-1),
        'OH':np.zeros(len(rspace)-1),
        'OFe':np.zeros(len(rspace)-1),
        'HH':np.zeros(len(rspace)-1),
        'HFe':np.zeros(len(rspace)-1),
        'FeFe':np.zeros(len(rspace)-1)
        }
for key, value in dict1.items():
    pair = key
    distances = value
    for i in range(len(rspace)-1):
        r = rspace[i]
        r_plus_dr = rspace[i+1]
        N=0
        for j in range(len(distances)):
            N=+1
            if distances[j] >= r and distances[j] < r_plus_dr:
                dict2[pair][i] += 1
        if dict2[pair][i] != 0:
            dict2[pair][i] = dict2[pair][i]/N
            dict2[pair][i] = dict2[pair][i]/(4*np.pi*(r**2)*dr)
            dict2[pair][i] = dict2[pair][i]/(len(distances)/15.52125**3)
        
        
            
        
        
    
    
            
import matplotlib.pyplot as plt
#histogram please copilot
x = rspace[:-1]
y = dict2['OFe']
plt.figure()
plt.plot(x,y)
plt.show()