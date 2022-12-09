import numpy as np
import matplotlib.pyplot as plt

ff_data = np.loadtxt('/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_angles.dat')
aimd_data = np.loadtxt('//Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/aimd_feoh_angle.dat')
nnp_data = np.loadtxt('/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/angles_from_nnp.dat')
newffdata= np.loadtxt('/Users/kitjoll/anglesnewffyeahboi.dat')
print(len(ff_data))
#make a histogram for each of ff, aimd and nnp data
#plot histogram of angles and number of atoms in each
plt.figure()
n, bins, patches = plt.hist(ff_data[:,1], 100, density=True, facecolor='g')
plt.xlabel('Angle')
plt.title('Histogram of angles for Fe-O-H in first solvation shell - FF')
plt.xlim(90,150)
plt.show()

plt.figure()
aimd_data = aimd_data[:,1]
aimd_data = aimd_data[815:]
a, b, c = plt.hist(aimd_data, 100, density=True, facecolor='r')
plt.xlabel('Angle')
plt.xlim(100,150)
plt.title('Histogram of angles for Fe-O-H in first solvation shell - AIMD') 
plt.show()

plt.figure()
x, y, z = plt.hist(nnp_data[:,1], 100, density=True, facecolor='b')
plt.xlabel('Angle')
plt.xlim(90,150)
plt.title('Histogram of angles for Fe-O-H in first solvation shell - NNP')
plt.show()

new_dat = newffdata[:,1]
print(len(new_dat))
new_dat = new_dat[815:]
p, q ,r = plt.hist(new_dat, 100, density=True, facecolor='y')
plt.xlabel('Angle')
plt.xlim(90,150)
plt.title('Histogram of angles for Fe-O-H in first solvation shell - new FF')
plt.show()



newffdata= np.loadtxt('/Users/kitjoll/moreanglesforyourboi.dat')
print(len(newffdata))
newnewdat = newffdata[:,1]
newnewdat = newnewdat[141019:143009]
p, q ,r = plt.hist(newnewdat, 100, density=True, facecolor='y')
plt.xlabel('Angle')
plt.xlim(95,150)
plt.title('Histogram of angles for Fe-O-H in first solvation shell - equilibrated FF')
plt.show()