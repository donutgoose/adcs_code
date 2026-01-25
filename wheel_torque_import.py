import math
import numpy as np
import matplotlib.pyplot as plt

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

def pseudoinverse(A):
    B = A.T
    return B.T @ np.linalg.inv(B @ B.T)

def wheel_torque_commands(A,t):
    return pseudoinverse(A) @ t

