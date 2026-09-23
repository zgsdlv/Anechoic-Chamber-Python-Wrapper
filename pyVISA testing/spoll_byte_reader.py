# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 15:23:59 2025

@author: leviresearch
"""

import pyvisa
import time


rm = pyvisa.ResourceManager()

#print(rm.list_resources())


# should be 3 since that's what its pins on the back have it set to
controller = rm.open_resource('GPIB0::3::INSTR')
controller.read_termination = '\r\n'
controller.write_termination = '\r\n' # this is specific to this controller
controller.baud_rate = 9600 # if i< gives S001, but if i< gives S003, = 2400


controller.write('FT1<')

# this binary converter will only be here until I find a pyVISA way to pull
# binary values instead of decimal

spoll_byte_decimal = controller.read_stb()
spoll_byte = ''
while spoll_byte_decimal > 0 :
    spoll_byte = str(spoll_byte_decimal & 1) + spoll_byte
    spoll_byte_decimal >>= 1
    
print(spoll_byte)


controller.close()