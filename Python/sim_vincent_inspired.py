import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib
import numpy as np
import os
from scipy.signal import find_peaks, peak_prominences
from scipy.optimize import curve_fit
from scipy.integrate import solve_bvp




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


def temp_profile(a, f_v, d, p, I):
    
    #Hydrogen beam flux profile in molecules per area and unit time [1/(s*m^2)]
    # r = radial distance from nozzle outlet axis
    # D = distance of the observation plane to nozzle 
    # f = hydrogen flow through the nozzle orifice in molecules per unit time
    
    f = (f_v*A_v)/(V_m*60) #hydrogen flow [1/s]
    
    def j(r, D, f):
        return (f/np.pi)*(D**2/(D**2+r**2)**2)

    #Flux of atoms due to the background pressure in ideal gas approximation [1/(s*m^2)]
    j_BG = p/(4*k_B*T_c)*np.sqrt((8*k_B*T_c)/(np.pi*m_H2))    


    #Prefactors when equation is grouped in the form: d^2T/dx^2 = A(x)*T(x) + B*T(x)^4 + C(x)

    def A(x):
        A = (-1/(k*A_cs))*((I**2 * (rho/A_cs))*a_R # Probe current heating 
        - (1 - diss)*phi*d*0.5*5*k_B*beta # beam gas cooling H_2
        - 2*diss*phi*d*0.5*3*k_B  # beam gas cooling H (*beta but specifically for H)
        - beta * pi * d * (P_Ch/(4*k_B*T_C))*math.sqrt((8*k_B*T_C/(pi*m_H_2)))*(5*k_B/2)) # Bkg cooling
        return A


    B = - (-1/(k*A_cs))*pi * d * e_W *o # wire radiative cooling 
    

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
    
    x_test = np.array([0.0])

    print("A =", A(x_test)[0])
    print("B =", B)
    print("C =", C(x_test)[0])    

    # ODE system first order:
    # y[0] = T
    # y[1] = dT/dx
    def ode(x, y):
        T = y[0]
        dTdx = y[1]
    
        d2Tdx2 = A(x)*T + B*T**4 + C(x)
    
        return np.vstack((dTdx, d2Tdx2))
    
    T0 = T_c
    L = l/2
    
    # boundry conditions
    def bc(ya, yb):
        return np.array([
            ya[0] - T0,   # T(-L) = T0
            yb[0] - T0    # T(+L) = T0
        ])
    
    # starting grid
    x = np.linspace(-L, L, 1000)
    
    # starting estimate
    y_guess = np.zeros((2, x.size))
    y_guess[0] = T0 + 1000*(1-(x/L)**2)
    
    sol = solve_bvp(ode, bc, x, y_guess, tol=1e-8, max_nodes=50000)
    
    if not sol.success:
        print("Keine Konvergenz:", sol.message)
    print(sol.status)
    print(sol.message)
        
    # check of symmetry
    print("T'(0) =", sol.sol(np.array([0]))[1][0])
    
    # evaluation
    x_plot = np.linspace(-L, L, 1000)
    T_plot = sol.sol(x_plot)[0]
    #plt.plot(x_plot, T_plot)
    #plt.xlabel("x")
    #plt.ylabel("T(x)")
    #plt.grid()
    #plt.show()
    
    print("Anzahl Knoten:", len(sol.x))
    
    '''
    plt.figure()
    plt.plot(sol.x, np.zeros_like(sol.x), "o")
    plt.title("Mesh points")
    '''
    T_mean = sum(T_plot)/len(T_plot)
    return T_plot, T_mean
    

def wire_res(a, f_v, d, p, I):
    T_mean_0 = temp_profile(0, f_v, d, p, I)[1]
    T_mean = temp_profile(a, f_v, d, p, I)[1]
    R_mean_0 = r_0*l/(np.pi*(d/2)**2)*(1+a_r*(T_mean_0-T_0))
    R_mean = r_0*l/(np.pi*(d/2)**2)*(1+a_r*(T_mean-T_0))
    signal = (R_mean-R_mean_0)/R_mean_0
    return R_mean, signal


#d = 5e-6 #wire diameter [m]
#a = 0 #dissociation fraction
#f_v = 0 #0.37 #hydrogen flow [mln/min]
#p = 5e-3 #background pressure [Pa]


f_v_values = np.linspace(0, 1, 100)
res_values = np.zeros(100)
signal_values = np.zeros(100)
x_plot = np.linspace(-l/2, l/2, 1000)
'''
for i in range(len(f_v_values)):
    res = wire_res(0, f_v_values[i], 5e-6, 5e-3, 1e-3)[0]
    #res_a = wire_res(0.1, 0.37, 5e-6, 5e-3, i_values[i])
    
    res_values[i] = res
'''
'''
temp_p = temp_profile(0, 0.4, 15e-6, 0.1, 1)[0]
plt.plot(x_plot, temp_p)    
'''    
    
'''
plt.plot(f_v_values, res_values, '-', marker='o', markerfacecolor='none', markersize=8)
#plt.plot(i_values*1e3, res_values_a, '-', marker='o', markerfacecolor='none', markersize=8)
plt.xlabel("Molecular Hydrogen flow in mln/min")
plt.ylabel("Wire resistance in Ohm")
'''


print("WIRE RES 15, a = 0, f = 0: " + str(wire_res(0, 0, 15e-6, 0.1, 1e-3)[0]))
print("WIRE RES 15, a = 0, f = 0.4: " + str(wire_res(0, 0.4, 15e-6, 1e-3, 1e-3)[0]))
print("DIFFERENCE: " + str(wire_res(0, 0.4, 15e-6, 0.1, 18e-3)[0]-wire_res(0, 0, 15e-6, 0.1, 18e-3)[0]))
#print("TEMP: " + str(temp_profile(0, 0, 15e-6, 1e-3, 1e-3)[1]))
#print("WIRE RES 16.5: " + str(wire_res(0, 0, 16.5e-6, 101325, 1e-3)[0]))


