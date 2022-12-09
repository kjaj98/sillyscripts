import numpy as np 
import matplotlib.pyplot as plt 
from parser import XYZParser
from box import Box as b

directory = '/Users/kitjoll/PHD/nnp/fe2_nnp/nnp_md_training/fifth_retrain/var_data'

data0=np.loadtxt(f'{directory}/var_data0')[:,1]
print('loaded 0')
data1=np.loadtxt(f'{directory}/var_data1')[:,1]
print('loaded 1')
data2=np.loadtxt(f'{directory}/var_data2')[:,1]
print('loaded 2')
data3=np.loadtxt(f'{directory}/var_data3')[:,1]
print('loaded 3')
data4=np.loadtxt(f'{directory}/var_data4')[:,1]
print('loaded 4')
data5=np.loadtxt(f'{directory}/var_data5')[:,1]
print('loaded 5')
data6=np.loadtxt(f'{directory}/var_data6')[:,1]
print('loaded 6')
data7=np.loadtxt(f'{directory}/var_data7')[:,1]
print('loaded 7')
data8=np.loadtxt(f'{directory}/var_data8')[:,1]
print('loaded 8')
data9 = np.loadtxt(f'{directory}/var_data9')[:,1]
print('loaded 9')

data=[data0,
data1,
data2,
data3,
data4,
data5,
data6,
data7,
data8,
data9
]
'''
ndirectory = '/Users/kitjoll/PHD/nnp/fe3_nnp/nnp_md_retrain/eighth/dats'
scatter_data0=np.loadtxt(f'{ndirectory}/config0.dat')[1]
scatter_data1=np.loadtxt(f'{ndirectory}/config1.dat')[1]
scatter_data2=np.loadtxt(f'{ndirectory}/config2.dat')[1]
scatter_data3=np.loadtxt(f'{ndirectory}/config3.dat')[1]
scatter_data4=np.loadtxt(f'{ndirectory}/config4.dat')[1]
scatter_data5=np.loadtxt(f'{ndirectory}/config5.dat')[1]
scatter_data6=np.loadtxt(f'{ndirectory}/config6.dat')[1]
scatter_data7=np.loadtxt(f'{ndirectory}/config7.dat')[1]
scatter_data8=np.loadtxt(f'{ndirectory}/config8.dat')[1]
scatter_data9=np.loadtxt(f'{ndirectory}/config9.dat')[1]
scatter_time0=np.loadtxt(f'{ndirectory}/config0.dat')[0]
scatter_time1=np.loadtxt(f'{ndirectory}/config1.dat')[0]
scatter_time2=np.loadtxt(f'{ndirectory}/config2.dat')[0]
scatter_time3=np.loadtxt(f'{ndirectory}/config3.dat')[0]
scatter_time4=np.loadtxt(f'{ndirectory}/config4.dat')[0]
scatter_time5=np.loadtxt(f'{ndirectory}/config5.dat')[0]
scatter_time6=np.loadtxt(f'{ndirectory}/config6.dat')[0]
scatter_time7=np.loadtxt(f'{ndirectory}/config7.dat')[0]
scatter_time8=np.loadtxt(f'{ndirectory}/config8.dat')[0]
scatter_time9=np.loadtxt(f'{ndirectory}/config9.dat')[0]

scatter_data = [
    scatter_data0,
scatter_data1,
scatter_data2,
scatter_data3,
scatter_data4,
scatter_data5,
scatter_data6,
scatter_data7,
scatter_data8,
scatter_data9
]
scatter_times = [scatter_time0,
scatter_time1,
scatter_time2,
scatter_time3,
scatter_time4,
scatter_time5,
scatter_time6,
scatter_time7,
scatter_time8,
scatter_time9]
'''
times=[
]
for i in range(len(data)):
    #calculate time array for each one 
    #first get the first two times 
    numbersteps =len(data[i])
    stepsize = 0.4999975
    final_time= numbersteps*stepsize
    tim = np.linspace(0, final_time ,len(data[i]))
    times.append(tim)
    
    
for i in range(len(data)):
    plt.figure()
    plt.plot(times[i],data[i])
    print(len(times[i]))
    #print(int(scatter_times[i]))
    #plt.scatter(times[i][int(scatter_times[i])],scatter_data[i],color='r')
    plt.savefig(f'{directory}/varplot{i}.png')
    
    
for  i in range(len(data)):
    lookingat = data[i]
    j=0
    while lookingat[j]<0.01:
        j+=1
    print(j)    
        
    


plot = False
if plot:
    plt.figure()
    for i in range(len(data)):
        plt.plot(times[i], data[i],label =f'Trajectory {i}')
        plt.savefig(f'var_plot{i}.png')
    plt.legend()
    plt.show()

'''

#now make it into a parallel one

#first make function
def do_stuff(label):
    dirt = '/Users/kitjoll/PHD/nnp/fe2_nnp/nnp_md_training/second_retrain/positions'
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
                            if np.linalg.norm(wrapped)<1.3:
                                writefile_at_frame(i,coord_arr)
                                print(f'There are two hydrogens less than 1.3 angstroms in frame {i} of trajectory {label}')
                                print(f"The index of the atoms are: {j} and {k}")  
                                index_of_frame = False 

                        if atom1type == 'O' and atom2type =='Fe':
                            if np.linalg.norm(wrapped)<1.64:
                                writefile_at_frame(i,coord_arr)
                                index_of_frame = False 
                                print(f'There is an Fe O pair less than 1.64 angstroms in frame {i} of trajectory {label}')
                                print(f"The index of the atoms are: {j} and {k}")   
                                
                        if atom1type == 'H' and atom2type =='Fe':
                            if np.linalg.norm(wrapped)<2.27:
                                writefile_at_frame(i,coord_arr)
                                index_of_frame = False 
                                print(f'There is an Fe H pair less than 2.27 angstroms in frame {i} of trajectory {label}')
                                print(f"The index of the atoms are: {j} and {k}")  

                        if atom1type == 'O' and atom2type =='O':
                            if np.linalg.norm(wrapped)<1.75:
                                writefile_at_frame(i,coord_arr)
                                index_of_frame = False 
                                print(f'There is an O O pair less than 1.75 angstroms in frame {i} of trajectory {label}')
                                print(f"The index of the atoms are: {j} and {k} in frame {i}")  
        i +=1
'''