import matplotlib.pyplot as plt 
import numpy as np 

path = '/Users/kitjoll/PHD/md_results/onetwofive_iron/fe_2_2000000steps/dimer-1.ener'
save_path = '/Users/kitjoll/PHD/md_results/onetwofive_iron/fe_2_2000000steps/'
data = np.loadtxt(path)
step = data[:,0]
time = data[:,1]
kinetic_ener = data[:,2]
temp = data[:,3]
pot_ener = data[:,4]
conserved_ener = data[:,5]


plt.figure(1)
plt.plot(step,temp)
plt.xlabel('step')
plt.ylabel(ylabel='Temperature (K)')
plt.xlim(0,step[-1])
plt.ylim(200,400)
plt.xlabel(xlabel='Step number of simulation')
plt.savefig(f'{save_path}/temp.png')

plt.show()


plt.figure(2)
plt.plot(step,pot_ener)
plt.xlim(0,step[-1])
#plt.ylim(-2.2,-1.7)
plt.ylabel(ylabel='Potential Energy (a.u.)')
plt.xlabel(xlabel='Step number of simulation')

plt.savefig(f'{save_path}/pe.png')
plt.show()
'''
plt.figure(3)
plt.plot(step,conserved_ener)
plt.xlim(0,step[-1])
plt.ylim(9.3975,9.41)
plt.ylabel(ylabel='Conserved quantity (a.u.)')
plt.savefig(f'{save_path}/conserved_convergence.pdf')
plt.show()
'''






