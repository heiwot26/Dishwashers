#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:54:16 2022

Collaborators; Nergez Brifkani, Heiwot Seyoum, Sambhav Kumar, Rubaba Noyireeta, Alexander Bilsland, Mohamed Darwish

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
psi = np.exp(-(x_array)**2)

#Calculates finite difference elements

dt = t_array[1] - t_array[0]
dx = x_array[1] - x_array[0]


#DEFINING NECASSARY FUNCTIONS

def run(psi):
    """Returns   """
    line.set_data(x_array, np.abs(psi)**2)
    return line,


def is_evaluable(userpoten):
    try:
        eval(userpoten)
        return True
    except:
        return False
    
    
    
def request_input(userpoten):
    print("Your input " + userpoten + " is not acceptable. Please choose a function in terms of only X")
    userpoten = str(input("Please choose a function to represent V(x), using the variable X:"))
    return userpoten



def user_input_X(userpoten):
    
    while is_evaluable(userpoten) == False: 
            userpoten = request_input(userpoten)
    else:
        if is_evaluable(userpoten) == True:
            userpoten = eval(userpoten)
            while isinstance(userpoten, np.ndarray) == False and isinstance(userpoten, int) == False:
                userpoten = request_input(userpoten)
            else:
                if isinstance(userpoten, np.ndarray) == True:
                    v_x = userpoten
                    return v_x
                elif isinstance(userpoten, int) == True:
                    v_x = np.array([userpoten]*Nx)
                    return v_x





def v_x_matrix_creator(v_x):
    v_x_matrix = diags(v_x)
    return v_x_matrix


    
def infinite_sqwell(userpoten, L):
    
    """
    Defines and returns an infinite square well when user wants an infinite square well.

    	Parameters:

            userpoten (str): Input function from the user

    	Returns:
		
    		V(x) (arr) : array representing the potential at every point of x/corresponding to x_array
    """
    
    v_x = np.zeros(Nx)
    v_x[400:Nx] = 10000
    v_x[0:100] = 10000
    v_x
    return v_x

def finite_sqwell(userpoten, N):
    
    """
    Defines and returns an finite square well when user wants an finite square well.

    	Parameters:
		
            N(float): height of the finite square well
            userpoten (str): Input function from the user

    	Returns:
		
            V(x) (arr) : array representing the potential at every point of x/corresponding to x_array
    
    """
    v_x = np.zeros(Nx)
    v_x[400:Nx] = N
    v_x[0:100] = N
    v_x
    return v_x

def step_function(userpoten, N):
    v_x = np.zeros(Nx)
    v_x[250:Nx] = N
    v_x
    return v_x


#define inputs

X = x_array

print("For infinite square well, please type infsqwell(). For finite square well, please type finsqwell() and define N, where N is the height. For a step function, please type stepfunc() and define N, where N is the height")
userpoten = str(input("Please choose a function to represent V(x), using the variable X:"))


    
#library to accept inputs

if 'sin' or 'cos' or 'tan' or 'pi' or '^' or 'exp' or 'arcsin' or 'arccos' or 'arctan' or 'sin^-1' or 'cos^-1' or 'tan^-1' or 'e' or 'sqrt' or 'log' in userpoten:
    userpoten = userpoten.replace('sin','np.sin')
    userpoten = userpoten.replace('cos','np.cos')
    userpoten = userpoten.replace('tan','np.tan')
    userpoten = userpoten.replace('sec','np.sec')
    userpoten = userpoten.replace('cosec','np.csc')
    userpoten = userpoten.replace('csc','np.csc') 
    userpoten = userpoten.replace('cotan','np.cot')
    userpoten = userpoten.replace('cot','np.cot')
    userpoten = userpoten.replace('arcsec','np.arcsec')
    userpoten = userpoten.replace('arccsc','np.arccsc')
    userpoten = userpoten.replace('arccot','np.arccot')  
    userpoten = userpoten.replace('sec^-1','np.arcsec')
    userpoten = userpoten.replace('csc^-1','np.arccsc')
    userpoten = userpoten.replace('cot^-1','np.arccot')  
    userpoten = userpoten.replace('arcsin','np.arcsin')
    userpoten = userpoten.replace('arccos','np.arccos')
    userpoten = userpoten.replace('arctan','np.arctan')   
    userpoten = userpoten.replace('sin^-1','np.arcsin')
    userpoten = userpoten.replace('cos^-1','np.arccos')
    userpoten = userpoten.replace('tan^-1','np.arctan')   
    userpoten = userpoten.replace('sqrt','(np.sqrt)')
    userpoten = userpoten.replace('pi','(np.pi)')
    userpoten = userpoten.replace(' ', '*')
    userpoten = userpoten.replace('^','**')
    userpoten = userpoten.replace('exp','np.exp')
    userpoten = userpoten.replace('log','np.log')
    


if userpoten == "infsqwell()":
    v_x = infinite_sqwell(userpoten, L)
    v_x_matrix = v_x_matrix_creator(v_x)
elif userpoten == "finsqwell()":
    N = str(input("Please input the height of the well N:"))
    N = eval(N)
    v_x = finite_sqwell(userpoten, N)
    v_x_matrix = v_x_matrix_creator(v_x)   
elif userpoten == "stepfunc()":
    N = str(input("Please input the height of the step N:"))
    N = eval(N)
    v_x = step_function(userpoten, N)
    v_x_matrix = v_x_matrix_creator(v_x)   
else:
    v_x = user_input_X(userpoten)
    v_x_matrix = v_x_matrix_creator(user_input_X(userpoten))
    



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
ani.save("particle_in_a_well12.mp4", fps=30, dpi=300) 