################################################################################
# Learning curves for energies and forces.
################################################################################
# Col  Name             Description
################################################################################
# 1    epoch            Current epoch.
# 2    RMSEpa_Etrain_pu RMSE of training energies per atom (physical units)
# 3    RMSEpa_Etest_pu  RMSE of test energies per atom (physical units)
# 4    RMSE_Etrain_pu   RMSE of training energies (physical units)
# 5    RMSE_Etest_pu    RMSE of test energies (physical units)
# 6    MAEpa_Etrain_pu  MAE of training energies per atom (physical units)
# 7    MAEpa_Etest_pu   MAE of test energies per atom (physical units)
# 8    MAE_Etrain_pu    MAE of training energies (physical units)
# 9    MAE_Etest_pu     MAE of test energies (physical units)
# 10   RMSE_Ftrain_pu   RMSE of training forces (physical units)
# 11   RMSE_Ftest_pu    RMSE of test forces (physical units)
# 12   MAE_Ftrain_pu    MAE of training forces (physical units)
# 13   MAE_Ftest_pu     MAE of test forces (physical units)
######################################################################################################################################################################################################################
#        1                2                3                4                5                6                7                8                9               10               11               12               13
#    epoch RMSEpa_Etrain_pu  RMSEpa_Etest_pu   RMSE_Etrain_pu    RMSE_Etest_pu  MAEpa_Etrain_pu   MAEpa_Etest_pu    MAE_Etrain_pu     MAE_Etest_pu   RMSE_Ftrain_pu    RMSE_Ftest_pu    MAE_Ftrain_pu     MAE_Ftest_pu
######################################################################################################################################################################################################################

import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt('/Users/kitjoll/PHD/Philipp_DFT_ML/python/runner2/learning-curve.out')

epoch = data[:,0]
RMSEpa_Etrain_pu = data[:,1]
RMSEps_Etest_pu = data[:,2]
RMSE_Etrain_pu = data[:,3]
RMSE_Etes_pu = data[:,4]
RMSE_Ftrain_pu = data[:,10]
RMSE_Ftest_pu = data[:,11]


plt.figure()
plt.plot(epoch, RMSE_Ftrain_pu)
plt.show()