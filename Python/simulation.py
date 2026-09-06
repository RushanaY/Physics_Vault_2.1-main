# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:04:19 2026

@author: rusha
# """

# Imporvement ideas 
#-> make function of plotting plot(important parameters (flux, pressure, solid angle?, temperature nozzle, diss ration (with and no plasma)))
# -> actually solve DEQ , copy from Vincent 
# -> 

# Other stuff
# -> do a general plotting of data, esp to compare stuff 

import matplotlib
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import os
from scipy.signal import find_peaks, peak_prominences
from scipy.optimize import curve_fit



# Constants
pi = math.pi # pi 
k_B = 1.380649e-23 # Boltzmann constant [m^2*^-2*K^-1] 
Av = 6.022e23 # Avogadros constant [1/mol]
o = 5.67e-8 # Stephan Boltzman constant [W*m^-2*K^-4]
m_H_2 = 3.346*10e-27           #kg # mass_hydrogen_mol 
rho = 5.6*10e-8              #Ω⋅m (at 20 °C) # electric resistivity 
k = 173                         #W/(m⋅K) # thermal conductivity
a_R = 0.0045                    #K-1 # temeprature coeffitient of resistivity
E_rec = 0.5 * 7.136 * 10e-20   #J # recomb_energy
e_W = 0.32                      # emmisivity of wire 
e_C = 0.07                      # emmisvity of copper at 20C

##########################################################################################################################################################################

# WIRE parameters 
d = 0.000005        #m # diameter 
A_cs = pi * d**2/4  # cross section 
t = 0.005           # m # distance to wire 
beta = 1            # accomodation factor 
L = 0.0036          #m # lenght wire 
D = 0.005 # distance of nozzle from wire [m]

#PLASMA parameters 
diss = 0.05          # diss_ratio


# HYDROGEN BEAM
V_m = 22.414e3 # molar volume [mln/mol]

# flux #to be extra calculated 
f = 0.37 
N_H2 = 1.66 * 10**7 #mol/s
# A_beam = t*pi*math.tan(pi/6)
# phi_t = N_H2/A_beam 
# flux undissaciciated 
phi = 6.33 * 10**21 

recomb_ratio_eta = 0.1 # recombination ratio

####################################################################################################################
# OTHER 

P_Ch = 5*10**-5 * 100    #mbar converted to pascal # pressure of chamber
I = 0.001 #A # probe_current

##########################################################################################################################################################################

# Temperatures 
# Hydrogen discharge 
T_H = 298 #K
# Nozzle 
T_N = 298 #K
# Chamber 
T_C = 298 #K 
# reference temperature for resistivity
T_ref = 293.15 #K 

##########################################################################################################################################################################
##########################################################################################################################################################################
# CALCULATION 

f_v = 0.37 
# hydrogen flow [1/s] calculated from flux [mlm/min]
f = (f_v * Av)/(V_m *60) 

# calcualte flux 
def j(r,D,f) :
	return (f/math.pi)*(D**2/(D**2+r**2)**2) 

# DEFINE COEFFICIENTS A, B, C
def A(x): 
    A = (-1/(k*A_cs))*((I**2 * (rho/A_cs))*a_R # Probe current heating 
    - (1 - diss)*phi*d*0.5*5*k_B*beta # beam gas cooling H_2
    - 2*diss*phi*d*0.5*3*k_B  # beam gas cooling H (*beta but specifically for H)
    - beta * pi * d * (P_Ch/(4*k_B*T_C))*math.sqrt((8*k_B*T_C/(pi*m_H_2)))*(5*k_B/2)) # Bkg cooling
    return A 



def B(x): 
    B = - (-1/(k*A_cs))*pi * d * e_W *o # wire radiative cooling 
    return B 



def C(x):
    C = (-1/(k*A_cs))*((I**2 * rho/A_cs 
    - (I**2 * (rho/A_cs))*a_R*T_ref# probe current heating # has the yet unkown T_ref 
    + (1 - diss)*phi*d*0.5*5*k_B*T_H # beam gas cooling
    + 2 * diss * phi*0.5*3*k_B*T_H*d  # beam gas cooling 
    + recomb_ratio_eta*E_rec*2*diss*phi *d # recombination heat 
    + beta * pi * d * (P_Ch/(4*k_B*T_C))*math.sqrt((8*k_B*T_C/(pi*m_H_2)))*(5*k_B/2)*T_C # bkg cooling 
    + pi*d*o*e_W *e_C* T_N**4 # nozzle cooling (S.thesis has it being positive)
    + pi*d*o*e_W*T_C**4)) # chamber cooling # sensible only if solid angle is considerd 

    return C

x_test = np.array([0])
print(A(x_test))
print(B(x_test))
print(C(x_test))


# ODE CALCULATION
def ode(x,y):
	T = y[0]
	dTdx = y[1]

	d2Tdx2 = A(x)*T + B*(T**4) + C(x)

	return np.vstack((dTdx, d2Tdx2))

T0 = T_C
L1 = L/2

# boundary conditions 
def bc(ya,yb): 
	return np.array([
	ya[0] - T0, #T(-L)
	yb[0] - T0  #T(L)
	])

# starting grid 
x = np.linspace(-L1,L1,1000)

# starting estimate 
y_guess = np.zeros((2,x.size))
y_guess[0]= T0 + 1000*(1-(x/L1)**2)

sol = solve_bvp(ode,bc, x, y_guess, tol=1e-8, max_nodes = 50000)

if not sol.success: 
	print("no convergence:", sol.message)
print(sol.status)
print(sol.message)

# check of symmetry
print("T'(0) = ", sol.sol(np.array([0]))[1][0])

# evaluation 
x_plot = np.linspace(-L, L, 1000)
T_plot = sol.sol(x_plot)[0]

print("number of nodes:" , len(sol.x))


T_mean = sum(T_plot)/len(T_plot)
#return T_plot, T_mean







