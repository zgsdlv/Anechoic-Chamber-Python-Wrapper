# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 15:09:09 2025

@author: leviresearch
"""

import pyvisa


lock = False
counter = 0

rm = pyvisa.ResourceManager()

lib = rm.visalib

rm.list_resources()

multimeter = rm.open_resource('GPIB0::16::INSTR')

print(multimeter.query('*IDN?'))

multimeter.read_termination

multimeter.read_termination = '\n'
multimeter.write_termination = '\n'
multimeter.baud_rate = 9600

sesh = multimeter.session

"""
noise_data = []
time_stamps = []

multimeter.write('FORMat:ELEMents READing, TSTamp')

while counter < 10:
    data = multimeter.query('READ?')
    #print(data)
    
    split_data = data.split(',')
    
    noise_data.append(split_data[0])
    time_stamps.append(split_data[1])
    
    time.sleep(0.01)
    counter += 1
    
print(noise_data)
print(time_stamps)

plt.plot(time_stamps, noise_data)
plt.show
"""


