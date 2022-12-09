import numpy as np
import matplotlib.pyplot as plt
#load data 



def plot_rdf(x,y,fig_name,atom1,atom2,path_to_save):
    plt.figure()
    plt.plot(x,y)
    plt.hlines(1,min(x),6,linestyles='dashed', colors='r')
    plt.ylabel('g(r)')
    plt.xlabel('r (Angstrom)')
    plt.xlim(0,6)
    plt.title(f'Radial Distribution Function for {atom1} and {atom2}')
    plt.savefig(f'{path_to_save}/{fig_name}.pdf')
    
oodata = '/Users/kitjoll/PHD/RDF_scripts/Soper/experimental/rdf_oo.dat'
hhdata = '/Users/kitjoll/PHD/RDF_scripts/Soper/experimental/rdf_hh.dat'
hodata = '/Users/kitjoll/PHD/RDF_scripts/Soper/experimental/rdf_oh.dat'
          
hosim = '/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/oh-rdf.dat'
hhsim = '/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/hh-rdf-sim.dat'
oosim = '/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/oo-sim-rdf.dat'

aimdoo = '/Users/kitjoll/PHD/aimd/fe3aq_traj/second_backup/oo-rdf-aimd.dat'
aimdhh='/Users/kitjoll/PHD/aimd/fe3aq_traj/second_backup/hh-rdf-aimd.dat'
aimdoh ='/Users/kitjoll/PHD/aimd/fe3aq_traj/second_backup/Oh-rdf-aimd.dat'


data = np.loadtxt(hodata)
data1 = np.loadtxt(hosim)
data2 = np.loadtxt(aimdoh)
x , y = data[:,0], data[:,1]
x1, y1 = data1[:,0],data1[:,1]
x2, y2 = data2[:,0],data2[:,1]
#paper_data = np.loadtxt('/Users/kitjoll/PHD/RDF_scripts/fe3_coord.txt',delimiter=',')
##x_paper, y_paper = paper_data[:,0], paper_data[:,1]
###y_paper = y_paper - min(y_paper)
#x_paper=np.insert(x_paper, 0, 0)
#y_paper=np.insert(y_paper, 0, 0)
fig_name = 'rdf_sim_data'
plt.figure()
plt.plot(x,y,label ='Experimental data - excluding intra-molecular')
plt.plot(x1,y1, label = 'NNP g(r)')
plt.plot(x2,y2, label = 'AIMD g(r)')
#ßplt.plot(x_paper, y_paper, label = 'B3LYP simulated g(r)')
plt.xlim(0,6)
plt.xlabel('r/angstrom')
plt.ylabel('g(r)')
plt.legend()
plt.title('Radial distribution function for O and H')
plt.show()




'''
path = '/Users/kitjoll/PHD/md_results/iron_simulation/new_inputs/output/ensuring_TIP3P/fe_H_rdf.dat'
data = np.loadtxt(path)
x,y = data[:,0], data[:,1]
fig_name='rdf_FeH'
plot_rdf(x,y,fig_name,'Fe','H', path_to_save)
/Users/kitjoll/PHD/errors
/Users/kitjoll/Library/Mobile Documents/com~apple~CloudDocs/PHD/errors
path = '/Users/kitjoll/PHD/md_results/iron_simulation/new_inputs/output/ensuring_TIP3P/gofr.dat'
path_to_save = '/Users/kitjoll/PHD/md_results/iron_simulation/new_inputs/output/ensuring_TIP3P'
data = np.loadtxt(path)
x , y = data[:,0], data[:,1]
path = '/Users/kitjoll/PHD/md_results/iron_simulation/new_inputs/output/ensuring_TIP3P/fe_H_rdf.dat'
data = np.loadtxt(path)
x1,y1 = data[:,0], data[:,1]
paper_data = np.loadtxt('/Users/kitjoll/PHD/RDF_scripts/fe3_coord.txt',delimiter=',')
x_paper, y_paper = paper_data[:,0], paper_data[:,1]

paper_data = np.loadtxt('/Users/kitjoll/PHD/RDF_scripts/coord_from_paper.txt',delimiter=',')
x_paper, y_paper = paper_data[:,0], paper_data[:,1]
y_paper = y_paper - min(y_paper)
x_paper=np.insert(x_paper, 0, 0)
y_paper=np.insert(y_paper, 0, 0)


#plot both rdfs on same graph
plt.figure()
plt.plot(x,y,label='Forcefield simulation')
#plt.plot(x1,y1, label='Fe-H',color ='g')
plt.plot(x_paper,y_paper, label='DFT paper',color='k')
plt.hlines(1,min(x),6,linestyles='dashed', colors='r',label='g(r)=1')
plt.xlim(0,6)
plt.legend()
plt.xlabel('r (Angstrom)')
plt.ylabel('g(r)')
plt.title('Radial Distribution Function for Fe-O ')

plt.savefig(f'{path_to_save}/rdf_FeO_andpaper_pres.png')

'''
