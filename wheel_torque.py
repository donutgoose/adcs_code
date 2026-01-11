import math
import numpy as np
import matplotlib.pyplot as plt

#a = 54.735
# FIX, math.sin USES RADIANS, double check all units
a = 45

target_torque = np.array([0.10, 0.00, 0.20])



def get_bases(a):
    b = math.radians(a)
    sin_a = math.sin(b)
    cos_a = math.cos(b)
    
    u_1 = np.array([cos_a, 0, sin_a])    
    u_2 = np.array([0, cos_a, sin_a])
    u_3 = np.array([-1*cos_a, 0, sin_a])
    u_4 = np.array([0, -1*cos_a, sin_a])
    B = np.array([u_1 ,u_2, u_3, u_4])
    
    return B

A = get_bases(a)

def pseudoinverse(A):
    B = A.T
    return B.T @ np.linalg.inv(B @ B.T)

def wheel_torque_commands(t):
    return pseudoinverse(A) @ t

tau_w = wheel_torque_commands(target_torque)
print(tau_w)

alpha = 45  # degrees
c = s = np.cos(np.radians(alpha))
B = np.array([
    [ c, 0, -c, 0],  # Roll
    [ 0, c, 0, -c],  # Pitch
    [ s, s, s,  s]   # Yaw
])



# Compute torque vectors in 3D
torque_vectors = B * tau_w  # each column is a wheel's contribution

# 3D plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

colors = ['r','g','b','orange']
for i in range(4):
    vec = torque_vectors[:,i]
    ax.quiver(*origin, *vec, color=colors[i], linewidth=2, arrow_length_ratio=0.1)
    ax.text(*(vec*1.1), f'Wheel {i+1}', color=colors[i])

ax.set_xlabel('Roll')
ax.set_ylabel('Pitch')
ax.set_zlabel('Yaw')
ax.set_title('3D Wheel Torque Contributions')
ax.set_xlim(-0.2, 0.2)
ax.set_ylim(-0.2, 0.2)
ax.set_zlim(-0.2, 0.4)

all_vectors = torque_vectors.flatten()
margin = 0.05  # add a little space around arrows
ax.set_xlim(all_vectors.min() - margin, all_vectors.max() + margin)
ax.set_ylim(all_vectors.min() - margin, all_vectors.max() + margin)
ax.set_zlim(all_vectors.min() - margin, all_vectors.max() + margin)

plt.show()

