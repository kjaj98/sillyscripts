import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
pi = np.pi

#function to select a random item from an array


hydrogen1 = np.array([0,0.81934,0.59365])
hydrogen2 = np.array([0,-0.81934,0.59365])

def make_random_rotation_matrix():  
    poss_angle = np.linspace(0, 2*pi, 100)
    #alpha, beta, gamma are the Euler angles
    #alpha is the rotation around the z axis
    #beta is the rotation around the x axis 
    #gamma is the rotation around the z axis
    alpha = np.random.choice(poss_angle)
    gamma= np.random.choice(poss_angle)
    beta = np.random.choice(poss_angle)
    r = R.from_euler('yxz', [alpha, beta, gamma], degrees=False)
    return r

def rotate_coord(coords):
    
    r = make_random_rotation_matrix()
    new_coords = []
    for i in coords:
        rotated_coords = r.apply(i)
        new_coords.append(rotated_coords)
    return np.array(new_coords)

coords = np.array([np.array([0,0,0]), hydrogen1, hydrogen2])

Test1 = False
if Test1:
    new_coords = rotate_coord(coords)
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(coords[:,0], coords[:,1], coords[:,2], color='red')
    ax.scatter(new_coords[:,0], new_coords[:,1], new_coords[:,2], color='blue')
    plt.show()

# function to check angle between two vectors
def angle_between_three_points(a, b, c):
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return angle


test2 = False
#check water angle is 104.45 degrees before and afer 
if test2:
    new_coords = rotate_coord(coords)
    angle= angle_between_three_points(coords[1], coords[0], coords[2])
    angle = np.rad2deg(angle)
    angle= angle_between_three_points(new_coords[1], new_coords[0], new_coords[2])
    angle = np.rad2deg(angle)


box_size = 125
box_length = np.cbrt(125/64*(12.417**3))
linspace= box_length/2
cube_root = int(round(box_size**(1/3)))
print(box_length)

possible_geometries=[]
for i in range(box_size):
    #create 100 rotated coords and store them in array called possible geometries
    possible_geometries.append(rotate_coord(coords))

#create 3d mesh grid of possible locations
[x,y,z] = np.meshgrid(np.linspace(-linspace,linspace,100), np.linspace(-linspace,linspace,100), np.linspace(-linspace,linspace,100))
#make a 3d grid of  64 points between -6.2085 and 5.2085    
[x1,y1,z1]= np.meshgrid(np.linspace(-linspace+1,linspace-1,cube_root), np.linspace(-linspace+1,linspace-1,cube_root), np.linspace(-linspace+1,linspace-1,cube_root))
#centre one of possibble_geometries on each point in the mesh grid
#flatten the mesh grid
flat = np.array([x1.flatten(), y1.flatten(), z1.flatten()]).T
#shift each geometry bby the coordinates in the mesh grid
xyzs = []
for i in range(box_size):
    xyz = []
    shift = flat[i]
    #check for clashes in xyzs and if there are none add to xyzs
    for j in range(3):
        xyz.append( possible_geometries[i][j] + shift)
    xyzs.append(xyz)
    
xyzs = np.array(xyzs)
xs=[]
ys=[]
zs=[]

for i in range(64):
    molec_cords = xyzs[i,:,:]
    for j in range(3):
        xs.append(molec_cords[j,0])
        ys.append(molec_cords[j,1])
        zs.append(molec_cords[j,2])

plottttt = False

if plottttt:
    fig = plt.figure(figsize=(14, 14))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs, ys, zs, color='blue')
    plt.show()

make_file = True

if make_file:
    #write name for file
    name = f"add_iron_to_me_{box_size}"
    #write text file with labels according to JB old file 
    with open(f'{name}.xyz', 'x') as f:
        f.write(f'{box_size*3}')
        f.write('\n')
        f.write('\n')
        for i in range(box_size):
            for j in range(3):
                atom = xyzs[i,j,:]
                x = atom[0]
                y =atom[1]
                z= atom[2]
                if j == 0:
                    atom = 'O'
                else:
                    atom = 'H'
                f.write("%s\t %s\t %s\t %s\t" % (atom, x, y, z))
                f.write('\n')


                
                
            