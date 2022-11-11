import numpy as np
import matplotlib.pyplot as plt
#from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation

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

x_array = np.linspace(xmin, xmax, Nx)
t_array = np.linspace(tmin, tmax, Nt)
psi = np.exp(-(x_array+2)**2)

dt = t_array[1] - t_array[0]
dx = x_array[1] - x_array[0]

def wavefunction_xt(x,t):
    timefac = np.exp((1j*E*t)/hbar)
    return (np.cos(k*x) + 1j*np.sin(k*x))*timefac

def Vsine(x):
    return np.sin(x)

def Vexpo(x):
    return np.exp(k*x)


userpoten = str(input("Please choose a function to represent V(x): sine or exponential. "))

while userpoten != 'sine' and userpoten != 'exponential':
    print("Please choose a function to represent V(x): sine or exponential. ")
    userpoten = str(input("Choose a function to represent V(x): sine or exponential. "))

else:
    if userpoten == 'sine':
        v_x = Vsine()
        v_x_matrix = diags(Vsine)
    elif userpoten == 'exponential':
        v_x = Vexpo()
        v_x_matrix = diags(Vexpo)

    

H = -0.5 * FinDiff(0, dx, 2).matrix(x_array.shape) + v_x_matrix

H[0, :] = H[-1, :] = 0
H[0, 0] = H[-1, -1] = 1

I_plus = eye(Nx) + 1j * dt / 2. * H
I_minus = eye(Nx) - 1j * dt / 2. * H
U = inv(I_minus).dot(I_plus)

psi_list = []
for t in t_array:
    psi = U.dot(psi)
    psi[0] = psi[-1] = 0
    psi_list.append(np.abs(psi))

psi_mag_squared = np.abs(psi_list)**2

fig, ax = plt.subplots()

ax.set_xlabel("x [arb units]")
ax.set_ylabel("$|\Psi(x, t)|$", color="C0")

ax_twin = ax.twinx()
ax_twin.plot(x_array, v_x, color="C1")
ax_twin.set_ylabel("V(x) [arb units]", color="C1")

line, = ax.plot([], [], color="C0", lw=2)
ax.grid()
xdata, ydata = [], []

def run(psi):
    line.set_data(x_array, np.abs(psi)**2)
    return line,

ax.set_xlim(x_array[0], x_array[-1])
ax.set_ylim(0, 1)

ani = animation.FuncAnimation(fig, run, psi_list, interval=10)
ani.save("particle_in_a_well.mp4", fps=120, dpi=300)