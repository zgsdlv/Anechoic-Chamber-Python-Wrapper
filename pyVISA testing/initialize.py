# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 11:31:51 2025

@author: leviresearch
"""

import pyvisa


rm = pyvisa.ResourceManager()

#print(rm.list_resources())

# should be 3 since that's what its pins on the back have it set to
controller = rm.open_resource('GPIB0::3::INSTR')
controller.read_termination = '\n'
controller.write_termination = '\n' # this is specific to this controller
controller.baud_rate = 9600 # if i< gives S001, but if i< gives S003, = 2400



def myWrite(controller, myCmd):
    controller.write('S')
    controller.write(myCmd)
    controller.write('H')
    
    controller.read() # NO QUOTATION MARKS!!!!!!!



# run the following two commands to shut down the controller

# controller.write('H')
# controller.close()