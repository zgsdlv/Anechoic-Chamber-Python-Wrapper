# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 16:48:03 2025

@author: leviresearch
"""

import matplotlib.pyplot as plt
import pyvisa
import time

lock = False
counter = 0

rm = pyvisa.ResourceManager()

lib = rm.visalib

multimeter = rm.open_resource('GPIB0::16::INSTR')

# to stop the error 213 beeping
multimeter.write('INIT:CONT OFF')

noise_data = []
time_stamps = []

multimeter.write('FORMat:ELEMents READing, TSTamp')

while counter < 100:
    data = multimeter.query_ascii_values('READ?')
    #print(data)
    
    noise_data.append(data[0])
    time_stamps.append(data[1])
    
    counter += 1
    
# since it was turned off earlier. Dont know if it needs to be back on but why not
multimeter.write('INIT:CONT ON')
    
print(noise_data)
print(time_stamps)

plt.plot(time_stamps, noise_data)
plt.title('Current Multimeter Readings')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.show