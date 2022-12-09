import numpy as np 
import matplotlib.pyplot as plt 
from parser import XYZParser
from box import Box as b

#now make it into a parallel one

#first make function
def do_stuff(label):
    dirt = '/Users/kitjoll/PHD/nnp/fe2_nnp/nnp_md_training/fourth_retrain/positions'
    def writefile_at_frame(i,coord_arr):
        with open(f'{dirt}/output{label}.xyz','w') as f:       
            f.write(str(len(coord_arr[i]['atoms']))+' ')
            f.write('\n')
            f.write(coord_arr[i]['comment'] + '')
            f.write('\n')
            for m in range(len(coord_arr[i]['atoms'])):
                f.write(coord_arr[i]['atoms'][m][0] + ' ' + str(coord_arr[i]['atoms'][m][1][0]) + ' ' + str(coord_arr[i]['atoms'][m][1][1]) + ' ' + str(coord_arr[i]['atoms'][m][1][2]) + '')
                f.write('\n')  
    box = b(cellfn = '/Users/kitjoll/PHD/Philipp_DFT_ML/python/nnp-md/cell.inc')
    coord_arr = XYZParser(f'{dirt}/pos{label}.xyz').to_array()
    index_of_frame = True
    i  = 0
    while index_of_frame:
        if i == len(coord_arr):
            index_of_frame = False
        
        if i>100:
            snapshot_coords = coord_arr[i]['atoms']
            for j in range(len(snapshot_coords)):
                for k in range(len(snapshot_coords)):
                    if k>j:
                        if index_of_frame:
                            atom1coords = snapshot_coords[j][1]
                            atom2coords = snapshot_coords[k][1]
                            atom1type = snapshot_coords[j][0]
                            atom2type = snapshot_coords[k][0]
                            v = np.subtract(atom1coords,atom2coords)
                            #wrap the box 
                            wrapped = box.pbc(v)
                            if np.linalg.norm(wrapped)<0.87:
                                print(f'There are two atoms less than 0.87 angstrom in frame {i} of trajectory {label}')
                                print(f"The index of the atoms are: {j} and {k}, the atoms are {atom1type} and {atom2type}")
                                writefile_at_frame(i,coord_arr)
                                index_of_frame = False 
                                
                            if atom1type == 'H' and atom2type =='H':
                                if np.linalg.norm(wrapped)<1.4:
                                    writefile_at_frame(i,coord_arr)
                                    print(f'There are two hydrogens less than 1.4 angstroms in frame {i} of trajectory {label}')
                                    print(f"The index of the atoms are: {j} and {k}")  
                                    index_of_frame = False 

                            if atom1type == 'O' and atom2type =='Fe':
                                if np.linalg.norm(wrapped)<1.9:
                                    writefile_at_frame(i,coord_arr)
                                    index_of_frame = False 
                                    print(f'There is an Fe O pair less than 1.9 angstroms in frame {i} of trajectory {label}')
                                    print(f"The index of the atoms are: {j} and {k}")   
                                    
                            if atom1type == 'H' and atom2type =='Fe':
                                if np.linalg.norm(wrapped)<2.27:
                                    writefile_at_frame(i,coord_arr)
                                    index_of_frame = False 
                                    print(f'There is an Fe H pair less than 2.27 angstroms in frame {i} of trajectory {label}')
                                    print(f"The index of the atoms are: {j} and {k}")  

                            if atom1type == 'O' and atom2type =='O':
                                if np.linalg.norm(wrapped)<2.25:
                                    writefile_at_frame(i,coord_arr)
                                    index_of_frame = False 
                                    print(f'There is an O O pair less than 2.25 angstroms in frame {i} of trajectory {label}')
                                    print(f"The index of the atoms are: {j} and {k} in frame {i}")  
        i +=1
