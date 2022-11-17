"""
Group Project

Collaborators; Rubaba Noyireeta, Nergez Brifkani, Mohamed Darwish, Alexander Bilsland, Sambhav Kumar, Heiwot Seyoum

"""

import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation

#Defines input parameters

Nx = 500 
xmin = -5
xmax = 5

Nt = 250
tmin = 0
tmax = 20

k = 1 
hbar = 1
m = 1
L = 16
E = (hbar**2)*(np.pi**2)/(2*m*L)

#Calculates grid, potential, and initial wave function

x_array = np.linspace(xmin, xmax, Nx)
t_array = np.linspace(tmin, tmax, Nt)
psi = np.exp(-(x_array+2)**2)

#Calculates finite difference elements

dt = t_array[1] - t_array[0]
dx = x_array[1] - x_array[0]

def wavefunction_xt(x,t):
    """Returns a wavefunction dependent on x and t"""
    timefac = np.exp((1j*E*t)/hbar) #Time Factor (t-dependance)
    return (np.cos(k*x) + 1j*np.sin(k*x))*timefac

def Vsine(x):
    """Returns a sine function, where the finite difference can be calculated"""
    return np.sin(x)
     

def Vexpo(x):
    """Returns an exponential function, where the finite difference can be calculated  """
    return np.exp(k*x)

def run(psi):
    """Returns   """
    line.set_data(x_array, np.abs(psi)**2)
    return line,

#Asks the user to choose a function to represent V(x) and runs the appropriation defined function

print("Choose a function to represent V(x) from the following options;")
print("\n[1] sin(x) , [2] exp(x)")
userpoten = str(input("Please enter a number, depending on the function you want to pick: "))

while userpoten != '1' and userpoten != '2': 
    print("\nInvalid Number entered!")
    userpoten = str(input("Please enter a number, depending on the function you want to pick: "))
else:
    if userpoten == '1':
            v_x = Vsine(x_array)
            v_x_matrix = diags(v_x)
    elif userpoten == '2':
            v_x = Vexpo(x_array)
            v_x_matrix = diags(v_x)

#Calculates the Hamiltonian matrix    

H = -0.5 * FinDiff(0, dx, 2).matrix(x_array.shape) + v_x_matrix

#Applies boundary condition to the Hamiltonian

H[0, :] = H[-1, :] = 0
H[0, 0] = H[-1, -1] = 1

I_plus = eye(Nx) + 1j * dt / 2. * H
I_minus = eye(Nx) - 1j * dt / 2. * H
U = inv(I_minus).dot(I_plus)

#Loops over each time, appending each calculation of psi to a list

psi_list = []
for t in t_array:
    psi = U.dot(psi)
    psi[0] = psi[-1] = 0
    psi_list.append(np.abs(psi))

psi_mag_squared = np.abs(psi_list)**2

#Plots the results

fig, ax = plt.subplots()

ax.set_xlabel("x [arb units]")
ax.set_ylabel("$|\Psi(x, t)|$", color="C0")

ax_twin = ax.twinx()
ax_twin.plot(x_array, v_x, color="C1")
ax_twin.set_ylabel("V(x) [arb units]", color="C1")

line, = ax.plot([], [], color="C0", lw=2)
ax.grid()
xdata, ydata = [], []


ax.set_xlim(x_array[0], x_array[-1])
ax.set_ylim(0, 1)

#Allows the program to make an MP4 file of the changing results.

ani = animation.FuncAnimation(fig, run, psi_list, interval=10)
ani.save("particle_in_a_well.mp4", fps=30, dpi=300) 