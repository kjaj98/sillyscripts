
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps


ff_dir='/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/new_plots/ff'
nnp_dir='/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/new_plots/nnp'
aimd_dir = '/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/new_plots/aimd'
save_dir = '/Users/kitjoll/PHD/nnp/fe3_nnp/test_nnp/ff_and_nnpmd_training/rdf_data/trialing_plots'

rdfs = ['feh','feo','hh','oh','oo']
titles = ['Fe-H','Fe-O','H-H','H-O','O-O']
ff_ds =[]
nnp_ds = []
for i in range(len(rdfs)):
    aimd_rdf = np.loadtxt(f'{aimd_dir}/{rdfs[i]}/rdf.dat')
    aimd_int = np.loadtxt(f'{aimd_dir}/{rdfs[i]}/int_rdf.dat')
    ff_rdf = np.loadtxt(f'{ff_dir}/{rdfs[i]}/rdf.dat')
    ff_int = np.loadtxt(f'{ff_dir}/{rdfs[i]}/int_rdf.dat')
    nnp_rdf = np.loadtxt(f'{nnp_dir}/{rdfs[i]}/rdf.dat')
    nnp_int = np.loadtxt(f'{nnp_dir}/{rdfs[i]}/int_rdf.dat')


    mod_diff_gr_ff = np.abs(aimd_rdf[:,1]-ff_rdf[:,1])    
    denominator_ff = simps(aimd_rdf[:,1],aimd_rdf[:,0])+ simps(ff_rdf[:,1],ff_rdf[:,0])
    integralz_ff = simps(mod_diff_gr_ff,aimd_rdf[:,0])
    
    mod_diff_gr_nnp = np.abs(aimd_rdf[:,1]-nnp_rdf[:,1])
    denominator_nnp = simps(aimd_rdf[:,1],aimd_rdf[:,0])+ simps(nnp_rdf[:,1],nnp_rdf[:,0])
    integralz_nnp = simps(mod_diff_gr_nnp,aimd_rdf[:,0])
    
    normff = 1 - (integralz_ff/denominator_ff)
    print(f'The norm of the RDF for the FF is {normff} for {titles[i]}')          
    ff_ds.append(normff)
    normnnp = 1- (integralz_nnp/denominator_nnp)
    print(f'The norm of the RDF for the NNP is {normnnp} for {titles[i]}')    
    nnp_ds.append(normnnp)
print(f'the avg norm for the FF is {np.mean(ff_ds)}')
print(f'the avg norm for the NNP is {np.mean(nnp_ds)}')      
        
