import numpy as np 
import scipy as sci

class Trajectory:
    def __init__(self, A, B, C, xyz_file, resolution =200, skip = 2):
        self.A = A
        self.B = B
        self.C = C
        self.xyz_file = xyz_file
        self.resolution = resolution
        self.skip = skip

        with open(self.xyz_file) as f:
            self.data = f.readlines()

        self.number_of_atoms = int(self.data[0])
        self.length_per_snapshot = self.number_of_atoms + 2
        self.snapshots=np.array([])
        self.number_of_snapshots = int(len(self.data)/self.length_per_snapshot)
        
        for j in range(0, self.number_of_snapshots, self.skip):
            self.snapshot = np.array([])
            for i in range(self.number_of_atoms):
                self.snapshot = np.append(self.snapshot, self.data[int(j*self.length_per_snapshot + 2 + i)])
            self.snapshots = np.append(self.snapshots, self.snapshot,0)
        
        self.number_of_snapshots = int(len(self.snapshots)/self.number_of_atoms)
        self.snapshots = self.snapshots.reshape(self.number_of_snapshots, self.number_of_atoms)
        
        self.atom_list = []
        for i in range(self.number_of_atoms):
            if self.snapshots[0][i].split()[0] not in self.atom_list:
                self.atom_list.append(self.snapshots[0][i].split()[0])
        #add in self.volumeperh2o
        self.volumeperh2o=0
                
                
                

    def extract_coordinates_of_snapshot(self,m):
        #extract coordinates for each atom type
        coords = np.array([])
 
        number_of_element = np.zeros(len(self.atom_list))

        for k,atom in enumerate(self.atom_list):
            for i in range(self.number_of_atoms):
                coords_per_atom_type = np.array([])
                if self.snapshots[0][i].split()[0] == atom:
                    number_of_element[k] += 1
                    coords_per_atom_type = np.append(coords_per_atom_type, self.snapshots[m][i])
                coords = np.append(coords, coords_per_atom_type)
        number_of_element = [int(i)for i in number_of_element]
        new_coords = []
        start = 0
        for i in range(len(number_of_element)):
            new_coords.append(coords[start:number_of_element[i]+start])
            start = number_of_element[i]+start
            
        for i, atom in enumerate(self.atom_list):
            if atom == 'O':
                number_of_water_per_snapshot = int(number_of_element[i])
        
        number_of_waters_considered = int(number_of_water_per_snapshot*self.number_of_snapshots)
        self.volumeperh2o =  (self.A*self.B*self.C)/number_of_waters_considered
                
        return new_coords
    
    def extract_coordinates_of_all_snapshots(self):
        coords_at_each_time_step =[]
        for i in range(self.number_of_snapshots):
            coords = self.extract_coordinates_of_snapshot(i)
            coords_at_each_time_step.append(coords)
        return coords_at_each_time_step
    
    def volume(self, r):
        """ volume of a sphere of radius r located at height z """
        volume = 4.0 / 3.0 * np.pi * r**3
        return volume
 
    def distance(self,a, b):
        """ get displacement in each coordinate and wrap w.r.t. lattice parameter """
        dx = abs(a[0] - b[0])
        x = min(dx, abs(self.A - dx))
        
        dy = abs(a[1] - b[1])
        y = min(dy, abs(self.B - dy))
        
        dz = abs(a[2] - b[2])
        z = min(dz, abs(self.C - dz))
        
        return np.sqrt(x**2 + y**2 + z**2)
    
    def compute_rdf(self,atom1,atom2):
        for i in range(len(self.atom_list)):
            if self.atom_list[i] == atom1:
                atom1_index = i
            if self.atom_list[i] == atom2:
                atom2_index = i
        coords_at_each_time_step = self.extract_coordinates_of_all_snapshots()
        
        r_cutoff = min(self.A, self.B) / 2.0
        dr = r_cutoff / self.resolution
        volumes = np.zeros(self.resolution)
         
        self.radii = np.linspace(0.0, self.resolution * dr, self.resolution)
        self.g_of_r = np.zeros(self.resolution)
        
        #iterate over each snapshot
        distances_between_atom1_and_atom2 = np.array([])
        for i in range(len(coords_at_each_time_step)):
            snapshot_coord = coords_at_each_time_step[i]
            atom1_data = snapshot_coord[atom1_index]
            atom2_data  = snapshot_coord[atom2_index]
            
            #for each snapshot find distance between each pair of atom1 and atom2 and store in a list
            distances_between_atom1_and_atom2_at_snapshot = []
            for k  in range(len(atom1_data)):
                for j in range(len(atom2_data)):
                    coords1 = (atom1_data[k].split()[1:])
                    coords2 = (atom2_data[j].split()[1:])
                    coords1 = [float(i) for i in coords1]
                    coords2 = [float(i) for i in coords2]
                    distance = self.distance(coords1, coords2)
                    distances_between_atom1_and_atom2_at_snapshot.append(distance)
            
            distances_between_atom1_and_atom2 = np.append(distances_between_atom1_and_atom2, distances_between_atom1_and_atom2_at_snapshot)
        for i in range((self.resolution)):
            #calculate the volume of each shell
            r1  = i * dr
            r2 =r1+dr
            v1 = self.volume(r1)
            v2 = self.volume(r2)
            volumes[i] = v2 - v1
        
        #loop over distances
        for i in range(len(distances_between_atom1_and_atom2)):
            index = int(distances_between_atom1_and_atom2[i] / dr)
            if 0<index<self.resolution:
                self.g_of_r[index] += 1.0
        
        for i, value in enumerate(self.g_of_r):
            self.g_of_r[i] = (value * self.volumeperh2o) / volumes[i]
            
        return self.radii, self.g_of_r
        
trajects = Trajectory(12.414,12.414,12.414, "/Users/kitjoll/PHD/md_results/iron_simulation/new_inputs/output/ensuring_TIP3P/dimer-pos-1.xyz", 300, 10)


coords = trajects.extract_coordinates_of_all_snapshots()
radii,g_of_r = trajects.compute_rdf('Fe', 'O')

import matplotlib.pyplot as plt 

plt.figure()
plt.plot(radii, g_of_r)
plt.show()
