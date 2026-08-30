import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib
import numpy as np
import os
from scipy.signal import find_peaks, peak_prominences
from scipy.optimize import curve_fit
from scipy.integrate import solve_bvp

#general constants
k_B = 1.38e-23 #Boltzmann constant[m^2*kg^-2*K^-1]
E_rec = (4.46/2)*1.6022e-19 #recombination enery of H2 per H atom (=> factor of 2) [J]
m_H2 = 3.35e-27 #mass of Hydrogen molecule [kg]
A_v = 6.022e23 #Avogadros constant [1/mol]
s = 5.67e-8 #Stefan Boltzmann constant [W*m^-2*K^-4]
e_T = 0.2 #0.32 #emmissivity Tungsten
e_C = 1 #emissivity Copper/Chamber 

#wire parameters
d_w = 5e-3 #distance of the wire detector to the nozzle [m]
l = 36e-3 #wire length [m]
k_0 = 174 #thermal conductivity (Tungsten) @ 20°C (T_0) [W*m^-1*K^-1]
a_k = -4.3e-4 #temperature coefficient of thermal conductivity @20°C (T_0) [1/K]
r_0 = 5.2e-8 #specific resistivty (Tungsten) @ 20°C (T_0) [Ohm*m]
a_r = 4.9e-3 #temperature coefficient of electrical resistivity @20°C (T_0) [1/K]
T_0 = 293.15 #20°C reference temperature for the specific resistivity & thermal conductivity [K]
k = k_0

#probe current 
#I = 1e-3 #[A]

#nozzle parameters 
T_n = 293.15 #nozzle temperature [K]


#hydrogen beam parameters
V_m = 22.414e3 #molar volume [mln/mol]
b_H2 = 1  #accomodation coefficient of H2 on the wire
n_rec = 0.1 #H recombination coefficient on Tungsten

#chamber parameters
T_c = 293.15 #chamber temperature [K]


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
        A = -(I**2*r_0*a_r*16)/(np.pi**2*k*d**4) + (2*(1-a)*5*k_B*j(x, d_w, f)*b_H2)/(d*np.pi*k) + (4*a*j(x, d_w, f)*3*k_B)/(d*np.pi*k) + (2*b_H2*5*k_B*j_BG)/(k*d)
        return A

    B = (4*s*e_T)/(d*k) #prefactor B doesn't depend on x

    def C(x):
        C = - (I**2*r_0*16)/(np.pi**2*k*d**4) + (I**2*r_0*a_r*16*T_0)/(np.pi**2*k*d**4) - (2*(1-a)*5*k_B*j(x, d_w, f)*T_n)/(d*np.pi*k) - (4*a*j(x, d_w, f)*3*k_B*T_n)/(d*np.pi*k) - (8*n_rec*E_rec*a*j(x, d_w, f))/(d*np.pi*k) - (4*s*e_T*e_C*T_c**4)/(d*k) - (2*b_H2*5*k_B*j_BG*T_c)/(k*d)
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


