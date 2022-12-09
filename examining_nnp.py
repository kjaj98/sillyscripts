import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('/Users/kitjoll/PHD/Philipp_DFT_ML/python/runner2/nnforces_longtrain.out')


pred_forces = [data[:,0],data[:,1],data[:,2]]
dft_forces = [data[:,3],data[:,4],data[:,5]]

ratios_x = np.zeros(len(pred_forces[0]))
ratios_y = np.zeros(len(pred_forces[0]))
ratios_z = np.zeros(len(pred_forces[0]))


for i in range(len(pred_forces[0])):
    #extract forces
    dft_force_x = dft_forces[0][i]
    dft_force_y = dft_forces[1][i]
    dft_force_z = dft_forces[2][i]
    pred_force_x = pred_forces[0][i]
    pred_force_y = pred_forces[1][i]
    pred_force_z = pred_forces[2][i]
    #calculate error abs(measured-real)/abs(real)
    ratios_x[i]= abs(pred_force_x-dft_force_x)/abs(max(pred_force_x,dft_force_x))
    ratios_y[i]= abs(pred_force_y-dft_force_y)/abs(max(pred_force_y,dft_force_y))
    ratios_z[i]= abs(pred_force_z-dft_force_z)/abs(max(pred_force_z,dft_force_z))

worst_x_erorr_index= np.where(ratios_x==max(ratios_x))
print(worst_x_erorr_index)
print((pred_forces[0][worst_x_erorr_index]))

'''
plt.figure()
plt.plot(atom_index,ratios_x,label='f_x')
plt.plot(atom_index,ratios_y,label='f_y')
plt.plot(atom_index,ratios_z,label='f_z')
plt.hlines(1, 0, 376,linestyles='dashed',colors='r')
plt.legend()
plt.show()
'''
