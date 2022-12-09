import matplotlib.pyplot as plt 
import numpy as np 

path = '/Users/kitjoll/PHD/nnp/fe2_nnp/nnp_md_training/fourth_retrain/ener_data'
save_path = '/Users/kitjoll/PHD/nnp/fe2_nnp/nnp_md_training/fourth_retrain/ener_data/plots'

ener_dir = '/Users/kitjoll/PHD/nnp/fe2_nnp/nnp_md_training/fourth_retrain/ener_data'


data = np.loadtxt(f'/Users/kitjoll/PHD/aimd/fe3aq_traj/second_backup/aimd-1.ener')
step = data[:,0]
time = data[:,1]
kinetic_ener = data[:,2]
temp = data[:,3]
pot_ener = data[:,4]
conserved_ener = data[:,5]
plt.plot(step,temp)
plt.show()


'''
for i in range(10):
    data = np.loadtxt(f'{ener_dir}/ener_data{i}')
    step = data[:,0]
    time = data[:,1]
    kinetic_ener = data[:,2]
    temp = data[:,3]
    pot_ener = data[:,4]
    conserved_ener = data[:,5]


    plt.figure()
    plt.plot(step,temp)
    plt.xlabel('step')
    plt.ylabel(ylabel='Temperature (K)')
    plt.xlim(0,step[-1])
    #plt.ylim(200,400)
    plt.xlabel(xlabel='Step number of simulation')
    plt.savefig(f'{save_path}/temp{i}.png')
    plt.close()


    plt.figure()
    plt.plot(step,pot_ener)
    plt.xlim(0,step[-1])
    #plt.ylim(-2.2,-1.7)
    plt.ylabel(ylabel='Potential Energy (a.u.)')
    plt.xlabel(xlabel='Step number of simulation')
    plt.savefig(f'{save_path}/pe{i}.png')
    plt.close()
    plt.figure()
    plt.plot(step,conserved_ener)
    plt.ylabel('Conserved quantitiy (a.u.)')
    plt.xlabel('Step number of simulation')
    plt.savefig(f'{save_path}/conserved{i}.png')
    plt.close()
    plt.figure()
    plt.plot(step, kinetic_ener)
    plt.ylabel('Kinetic energy (a.u.)')
    plt.xlabel('Step number of simulation')
    plt.savefig(f'{save_path}/kinetic{i}.png')
    plt.close()
'''