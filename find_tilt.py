import numpy as np 
import matplotlib.pyplot as plt
from parser import XYZParser
from box import Box as b
box = b(cellfn = '/Users/kitjoll/PHD/Philipp_DFT_ML/python/nnp-md/cell.inc')


def find_tilt_angles(path,vector_indicies):
    #path_to_file=input('Enter the path to the file: ')
    coords = XYZParser(f'{path}').to_array()
    debugging = False
    angles = np.empty(len(coords))  
    doit = True
    i=0
    while doit:
        if i == len(coords):
            break
        #read the coords
        frame = coords[i]
        xyzcoords = frame['atoms']
        newshiz = []
        for j in range(len(vector_indicies)):
            index_to_track = vector_indicies[j]
            for m in range(len(index_to_track)):
                newcoords = xyzcoords[int(index_to_track[m])]
                newshiz.append(newcoords)
            o = np.subtract(newshiz[0][1],newshiz[0][1])
            ofe = box.pbc(np.subtract(newshiz[3][1],newshiz[0][1]))
            oh1 = box.pbc(np.subtract(newshiz[1][1],newshiz[0][1]))
            oh2 = box.pbc(np.subtract(newshiz[2][1],newshiz[0][1]))
            norm_to_plane = np.cross(oh1,oh2)
            norm_norm_to_plane = np.linalg.norm(norm_to_plane)
            norm_to_plane = norm_to_plane/norm_norm_to_plane
            theta = np.arccos(np.dot(ofe, norm_to_plane) / (np.linalg.norm(ofe) * np.linalg.norm(norm_to_plane)))
            angles[i] = (90-np.rad2deg(theta))

            
        if debugging:
            print(newshiz)    
            print(newshiz[0][0],newshiz[3][0])
            print(ofe)
            print(box.pbc(ofe))
            fig = plt.figure(figsize=(12, 12))
            ax = fig.add_subplot(projection='3d')
            ax.scatter([o[0],oh1[0],oh2[0],halfwayhouse[0]], [o[1],oh1[1],oh2[1],halfwayhouse[1]], [o[2],oh1[2],oh2[2],halfwayhouse[2]], color='r')
            plt.show()    
        

        i+=1
    return angles


def find_feoh_angles(path,vector_indicies):
    #path_to_file=input('Enter the path to the file: ')
    coords = XYZParser(f'{path}').to_array()
    debugging = False
    angles = np.empty(len(coords))  
    angles2 =np.empty(len(coords))
    doit = True
    i=0
    while doit:
        if i == len(coords):
            break
        #read the coords
        frame = coords[i]
        xyzcoords = frame['atoms']
        newshiz = []
        for j in range(len(vector_indicies)):
            index_to_track = vector_indicies[j]
            for m in range(len(index_to_track)):
                newcoords = xyzcoords[int(index_to_track[m])]
                newshiz.append(newcoords)
            o = np.subtract(newshiz[0][1],newshiz[0][1])
            ofe = box.pbc(np.subtract(newshiz[3][1],newshiz[0][1]))
            oh1 = box.pbc(np.subtract(newshiz[1][1],newshiz[0][1]))
            oh2 = box.pbc(np.subtract(newshiz[2][1],newshiz[0][1]))
            theta1 = np.arccos(np.dot(ofe, oh1) / (np.linalg.norm(ofe) * np.linalg.norm(oh1)))
            theta2 = np.arccos(np.dot(ofe, oh2) / (np.linalg.norm(ofe) * np.linalg.norm(oh2)))

            angles[i] = (np.rad2deg(theta1))
            angles2[i] = (np.rad2deg(theta2))


            
        if debugging:
            print(newshiz)    
            print(newshiz[0][0],newshiz[3][0])
            print(ofe)
            print(box.pbc(ofe))
            fig = plt.figure(figsize=(12, 12))
            ax = fig.add_subplot(projection='3d')
            ax.scatter([o[0],oh1[0],oh2[0],halfwayhouse[0]], [o[1],oh1[1],oh2[1],halfwayhouse[1]], [o[2],oh1[2],oh2[2],halfwayhouse[2]], color='r')
            plt.show()    
        

        i+=1
    total_angles = np.append(angles,angles2)
    return total_angles

##############################
##############################
##############################


vector_indicies = [
[135,136,137,375],
[12,13,14,375],
[195,196,197,375],
[306,307,308,375],
[219,220,221,375],
[156,157,158,375]
]





path = '/Users/kitjoll/PHD/temp_data/iron_centre_box/centred_nnp.xyz'

angles = find_tilt_angles(path, vector_indicies)


aimdpath = '/Users/kitjoll/PHD/temp_data/iron_centre_box/centred_aimd.xyz'
ffpath = '/Users/kitjoll/PHD/temp_data/iron_centre_box/centred_ff.xyz'
aimd_indicies = [
[366, 367,  368, 375],
[306, 307,  308, 375],
[369, 370,  371, 375],
[78 , 79  ,  80, 375],
[315, 316,  317, 375],
[114, 115,  116, 375]]
ff_indicies = [
[12 , 13 , 14 ,375],
[306, 307, 308,375],
[81 , 82 , 83 ,375],
[87 , 88 , 89 ,375],
[318, 319, 320,375],
[45 , 46 , 47 ,375]   
]

angles1 = find_tilt_angles(aimdpath, aimd_indicies)
angles2 = find_tilt_angles(ffpath, ff_indicies)


######################################################################################
######################################################################################
'''

a, b, c = plt.hist(angles, bins=100, density=True)
a1, b1, c = plt.hist(angles1, bins=100, density=True)
a2, b2, c = plt.hist(angles2, bins=100, density=True)
plt.close()


bin_centers = 0.5*(b[1:]+b[:-1])
bin_centersa = 0.5*(b1[1:]+b1[:-1])
bin_centersb = 0.5*(b2[1:]+b2[:-1])

plt.plot(bin_centers,a, label='NNP')
plt.plot(bin_centersa,a1,label='AIMD')
plt.plot(bin_centersb,a2, label= 'FF')
plt.legend()
plt.xlabel('\u03B8/degrees')
plt.title('Histogram of angles for tilt plane in first solvation shell')
plt.show()


####################################
####################################
####################################

angles = np.abs(angles)
angles1 = np.abs(angles1)
angles2 = np.abs(angles2)


x,y,z = plt.hist(angles, bins=100, density=True)
x1,y1,z = plt.hist(angles1, bins=100, density=True)
x2,y2,z = plt.hist(angles2, bins=100, density=True)
plt.close()

bin_centers2 = 0.5*(y[1:]+y[:-1])
bin_centers2a = 0.5*(y1[1:]+y1[:-1])
bin_centers2b = 0.5*(y2[1:]+y2[:-1])

plt.figure()
plt.plot(bin_centers2,x, label = 'NNP')
plt.plot(bin_centers2a,x1, label = 'AIMD')
plt.plot(bin_centers2b,x2, label = 'FF')
plt.title('Probability density of |\u03B8| for tilt plane in first solvation shell')
plt.xlabel('\u03B8/degrees')
plt.legend()
plt.show()


##########################################
##########################################
##########################################


cos_angles = np.cos(np.deg2rad(angles))
cos_angles1 = np.cos(np.deg2rad(angles1))
cos_angles2 = np.cos(np.deg2rad(angles2))


p,q,r = plt.hist(cos_angles,bins=100,density=True)
p1,q1,r = plt.hist(cos_angles1,bins=100,density=True)
p2,q2,r = plt.hist(cos_angles2,bins=100,density=True)
plt.close()

plt.figure()
bin_centers3 = 0.5*(q[1:]+q[:-1])
bin_centers3a = 0.5*(q1[1:]+q1[:-1])
bin_centers3b = 0.5*(q2[1:]+q2[:-1])
plt.plot(bin_centers3,p,label ='nnp')
plt.plot(bin_centers3a,p1 ,label ='aimd')
plt.plot(bin_centers3b,p2, label ='ff')
plt.title('Probability density of cos(\u03B8) for tilt plane in first solvation shell')
plt.xlabel('cos(\u03B8)')
plt.legend()
plt.show()
'''

##########################################
##########################################
##########################################
#### do it for feoh angle now ############


angles =  find_feoh_angles(path, vector_indicies)
angles1 = find_feoh_angles(aimdpath, aimd_indicies)
angles2 = find_feoh_angles(ffpath, ff_indicies)


s, t, r = plt.hist(angles, bins=100, density=True)
s1,t1, r = plt.hist(angles1, bins=100, density=True)
s2,t2, r = plt.hist(angles2, bins=100, density=True)
plt.close()


bin_centerst =  0.5*(t[1:]+ t[:-1])
bin_centersta = 0.5*(t1[1:]+t1[:-1])
bin_centerstb = 0.5*(t2[1:]+t2[:-1])

plt.plot(bin_centerst,s, label='NNP')
plt.plot(bin_centersta,s1,label='AIMD')
plt.plot(bin_centerstb,s2, label= 'FF')
plt.legend()
plt.xlabel('\u03B8/degrees')
plt.title('Histogram of angles for Fe-O-H angle in first solvation shell')
plt.show()