import numpy as np
import matplotlib.pyplot as plt


ff_dir='/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/new_plots/ff'
nnp_dir='/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/new_plots/nnp'
aimd_dir = '/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/new_plots/aimd'
save_dir = '/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/trialing_plots'

rdfs = ['feh','feo','hh','oh','oo']
titles = ['Fe-H','Fe-O','H-H','H-O','O-O']
plot = False
if plot:
    for i in range(len(rdfs)):
        print(i)
        aimd_rdf = np.loadtxt(f'{aimd_dir}/{rdfs[i]}/rdf.dat')
        aimd_int = np.loadtxt(f'{aimd_dir}/{rdfs[i]}/int_rdf.dat')
        ff_rdf = np.loadtxt(f'{ff_dir}/{rdfs[i]}/rdf.dat')
        ff_int = np.loadtxt(f'{ff_dir}/{rdfs[i]}/int_rdf.dat')
        nnp_rdf = np.loadtxt(f'{nnp_dir}/{rdfs[i]}/rdf.dat')
        nnp_int = np.loadtxt(f'{nnp_dir}/{rdfs[i]}/int_rdf.dat')
        plt.figure()
        plt.title(f'{titles[i]} RDF')
        plt.xlabel('r/Å')
        plt.ylabel('g(r)')
        if titles[i]=='H-H':
            plt.ylim(0,4)
        elif titles[i]=='Fe-O':
            plt.ylim(0,20)
        elif titles[i]=='O-O':
            plt.ylim(0,5)
        elif titles[i]=='H-O':
            plt.ylim(0,35)
        else:
            plt.ylim(0,8)
        plt.plot(aimd_rdf[:,0],aimd_rdf[:,1],label='AIMD',color = 'red')
        plt.plot(aimd_int[:,0],aimd_int[:,1],label='AIMD integral',color = 'red',linestyle='dashed')
        plt.plot(ff_int[:,0],ff_int[:,1],label='FF integral',color = 'green',linestyle='dashed')
        plt.plot(ff_rdf[:,0],ff_rdf[:,1],label='FF',color = 'green')
        plt.plot(nnp_int[:,0],nnp_int[:,1],label='NNP integral',color = 'blue',linestyle='dashed')
        plt.plot(nnp_rdf[:,0],nnp_rdf[:,1],label='NNP', color = 'blue')
        plt.legend()
        plt.savefig(f'{save_dir}/{titles[i]}.png')        

newff = np.loadtxt('/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/newff_rdf.dat')
aimd_rdf = np.loadtxt(f'{aimd_dir}/feh/rdf.dat')
aimd_int = np.loadtxt(f'{aimd_dir}/feh/int_rdf.dat')
nnp_rdf = np.loadtxt(f'{nnp_dir}/feh/rdf.dat')
nnp_int = np.loadtxt(f'{nnp_dir}/feh/int_rdf.dat')
equibff_x = newff[:,0]
print(equibff_x[:len(equibff_x)])
print(equibff_x[-1])

plt.figure()
plt.plot(newff[500:,0],newff[500:,1], label = 'new ff')
plt.plot(aimd_rdf[:,0],aimd_rdf[:,1])
plt.plot(nnp_rdf[:,0],nnp_rdf[:,1])
plt.legend()
plt.show()