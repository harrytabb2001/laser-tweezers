#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:47:34 2022

@author: harrytabb
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('/Users/harrytabb/Desktop/Uni/Uni Year 3/Labs/Laser Tweezers/Lab Interview Stuff/power_csv.csv', dtype='float', delimiter=',')

power_errors = np.array([0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.01, 0.01, 0.01, 0.01])

def chi_squared_function(m_c, current, power, uncertainty):
    m = m_c[0]
    c = m_c[1]
    
    expected_power = m*current + c


    chi_square_equation = np.sum(((expected_power - power)
                                  / uncertainty)**2)
    
    return chi_square_equation

data = data[:,0:2]
data = data[:11]
data[0][0] = 35.12

currents = data[:,0]
powers = data[:,1:4]
power_errors = power_errors

avg_power = np.mean(powers, axis=1)

m, c = np.polyfit(currents, avg_power, deg=1, w=avg_power/power_errors)
chi_square= chi_squared_function([m,c], currents, avg_power, power_errors)
plt.figure()
plt.errorbar(currents, avg_power, yerr=power_errors, fmt='.', label='Data')
# plt.plot(currents, m*currents + c, label='Fit')
plt.xlabel('Current / mA')
plt.ylabel('Power / mW')
plt.legend()
plt.title('Plot of Current against measured Power for Laser')
plt.show()

print(m, c)
