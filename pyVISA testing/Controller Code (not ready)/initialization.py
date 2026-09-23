# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 17:50:11 2025

@author: leviresearch
"""

'''
This is the initialization script. This will run first and will define
everything.

No other script should ever modify the variables they use from this script, 
allowing it to be run whenever and not just once at the start and never again.
This is not because I dislike good design, this is because programming scares 
me.
'''

# THIS SCRIPT IS NOT READY DO NOT RUN IT

import pyvisa

rm = pyvisa.ResourceManager()

lib = rm.visalib


CONTROLLER_ID = 'to be determined'
resources = rm.list_resources()
controller_port = ''


for i in len(resources):
    repeats = 0
    resource = resources[i]
    to_query = rm.open_resource(resource)
    
    if to_query.query('*IDN?') == CONTROLLER_ID:
        controller_port = resource
        repeats += 1
        
    if repeats > 1:
        controller_port = ''
        
    try:
        1/len(controller_port)
        
    except:
        print('Found ' + str(repeats) + ' instances of expected controller')



instrument = rm.open_resource('GPIB0::16::INSTR') # global variable?

print(instrument.query('*IDN?')) # maybe use this to check it's the right ID?
# a way to do the checking:
# while programming, find the ID that the controller spits out. Then, record
# this as a variable, and have the system check to make sure it matches
# Going a step further, could have it so the script checks all ports returned
# by rm.list_resources(), and then finding the one that matches the ID. This
# way, no one needs to know how to set the correct ID depending on the port,
# and most importantly, no one needs but those working on this code need to
# ever look at this file


instrument.read_termination = '\n'
instrument.write_termination = '\n'
instrument.baud_rate = 9600

sesh = instrument.session


# note: the only variable that should be pulled from this file is instrument,
# which should not get changed ever, except in this file