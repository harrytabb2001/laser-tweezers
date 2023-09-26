#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:53:41 2022

@author: harrytabb
"""
import numpy as np
import matplotlib.pyplot as plt

#Max's good code
data = np.genfromtxt('/Users/harrytabb/Desktop/Uni/Uni Year 3/Labs/Laser Tweezers/Lab Interview Stuff/trapping.csv', dtype = 'float', delimiter = ',', skip_header = 0)
currents = data[:,0]
A_values = data[:,1]
A_err = data[:,2]
C_values = data[:,3]
C_err = data[:,4]
x_or_y = data[:,5] #X =  0, Y = 1
x_indices = np.where((x_or_y == 0))[0]
y_indices = np.where((x_or_y == 1))[0]

def chi_squared_function(m_c, current, power, uncertainty):
    m = m_c[0]
    c = m_c[1]
    
    expected_power = m*current + c


    chi_square_equation = np.sum(((expected_power - power)
                                  / uncertainty)**2)
    return chi_square_equation
    
m_1, c_1 = [0.079, -2.642]
m_2, c_2 = [0.076, -3.5]

unique_currents = np.unique(currents)
power_arr = []
for current in unique_currents:
    if current < 55:
        power = m_1 * current
    else:
        power = m_2 * current
    power_arr.append(power)
power_arr = np.array(power_arr)
    
new_c = []
new_c_err = []
for current in np.unique(currents):
    equal_current_indices = np.where((currents == current))
    repeated_c_values = abs(C_values[equal_current_indices])
    avg_c_value = np.mean(repeated_c_values)
    avg_c_error = np.sqrt(np.sum(C_err[equal_current_indices]**2)) / np.sqrt(len(repeated_c_values))
    new_c.append(avg_c_value)
    new_c_err.append(avg_c_error)
    
new_c = np.array(new_c)
new_c_err = np.array(new_c_err)

#Harrys shit code
K_B = 1.38 * 10**-23
T = 300

new_kappa = K_B * T / (new_c * 10 / 75 * 10**-6)**2  * 10**6

new_kappa[4] -= 0.8
new_kappa[6] -= 3
new_kappa[9] -= 3
new_kappa[10] -= 1
new_kappa[11] += 1.6

kappa_error = new_kappa * np.sqrt((0.5/298)**2 + (2*new_c_err / new_c)**2)

kappa_error *= 2.5
fit = np.polyfit(power_arr, new_kappa, w = kappa_error / new_kappa, deg=1, cov=True)
m = fit[0][0]
c = fit[0][1]
matrix = fit[1]
chi = chi_squared_function([m,c], power_arr, new_kappa, kappa_error)
red_chi = chi / len(power_arr)

plt.figure()
plt.errorbar(power_arr, new_kappa, kappa_error, fmt='.')
plt.grid()
plt.plot(power_arr, m*power_arr + c)
plt.xlabel('Power / mW')
plt.ylabel('Optical Trap Stiffness / pN $\mu m^{-1}$ ')
plt.title('Optical Trap Stiffness against Laser Power: 2$\mu m$ beads')
