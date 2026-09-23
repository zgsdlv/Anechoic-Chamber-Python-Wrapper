# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 14:27:52 2025

@author: leviresearch

note from charlie:
    
something is up with this code now. I think theres something to do with the
data stored in the buffers, but it seems to mix up which data to give to which
request. For example, I can run the code several times without changing
anything, and the results will change, until it reaches some kind of
equilibrium, which I know the results are wrong

basically, I need to clear the buffers, and get a better idea of how to
structure the code in a way that it handles the way the controller sends data
better. More research is required

Also, this test file is getting bloated. I need to start cleaning things up

Also, its not working for some reason. Wont give me any data back. Need to find
out how to clear the buffers before I can continue

Also also, simpler way for the boundary outputs is to cut off the character
at the start, and then divide the number by 100. No need to stitch it together
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




def read_boundaries():

    controller.write('H')
    controller.write('S')

    #print(instrument.query('Pas<', delay = 0.101))
    Pas_response = list(controller.query('Pas<', delay = 0.101))
    Pas_integers = ''.join([str(itm) for itm in Pas_response[1:-2]])
    Pas_decimals = ''.join([str(itm) for itm in Pas_response[-2:]])
    print('Starting position of raster scan is ' + Pas_integers + '.' + Pas_decimals + ' degrees')

    time.sleep(0.101)

    #print(instrument.query('Pab<', delay = 0.101))
    Pab_response = list(controller.query('Pab<', delay = 0.101))
    Pab_integers = ''.join([str(itm) for itm in Pab_response[1:-2]])
    Pab_decimals = ''.join([str(itm) for itm in Pab_response[-2:]])
    print('Ending position of raster scan is ' + Pab_integers + '.' + Pab_decimals + ' degrees')
    
    time.sleep(0.101)

    #print(instrument.query('Pat<', delay = 0.101))
    Pat_response = list(controller.query('Pat<', delay = 0.101))
    Pat_integers = ''.join([str(itm) for itm in Pat_response[1:-2]])
    Pat_decimals = ''.join([str(itm) for itm in Pat_response[-2:]])
    print('Track target of the first axis is ' + Pat_integers + '.' + Pat_decimals + ' degrees')
    
    time.sleep(0.101)

    #print(instrument.query('Pes<', delay = 0.101))
    Pes_response = list(controller.query('Pes<', delay = 0.101))
    Pes_integers = ''.join([str(itm) for itm in Pes_response[1:-2]])
    Pes_decimals = ''.join([str(itm) for itm in Pes_response[-2:]])
    print('Starting position of raster step is ' + Pes_integers + '.' + Pes_decimals + ' degrees')
    
    time.sleep(0.101)

    #print(instrument.query('Pab<', delay = 0.101))
    Peb_response = list(controller.query('Peb<', delay = 0.101))
    Peb_integers = ''.join([str(itm) for itm in Peb_response[1:-2]])
    Peb_decimals = ''.join([str(itm) for itm in Peb_response[-2:]])
    print('Ending position of raster step is ' + Peb_integers + '.' + Peb_decimals + ' degrees')
    
    time.sleep(0.101)

    #print(instrument.query('Pet<', delay = 0.101))
    Pet_response = list(controller.query('Pet<', delay = 0.101))
    Pet_integers = ''.join([str(itm) for itm in Pet_response[1:-2]])
    Pet_decimals = ''.join([str(itm) for itm in Pet_response[-2:]])
    print('Track target of second axis is ' + Pet_integers + '.' + Pet_decimals + ' degrees')
    
    controller.write('H')
    
    
    
def read_axis():    

    controller.write('H')
    controller.write('S')

    #print(controller.query('Aa<', delay = 0.101))
    Aa_response = list(controller.query('Aa<', delay = 0.101))
    print('Scan axis is set to ' + str(Aa_response[-1]))
    
    time.sleep(0.101)

    #print(controller.query('Ae<', delay = 0.101))
    Ae_response = list(controller.query('Ae<', delay = 0.101))
    print('Step axis is set to ' + str(Ae_response[-1]))
    
    time.sleep(0.101)

    #print(controller.query('Az<', delay = 0.101))
    Az_response = list(controller.query('Az<', delay = 0.101))
    print('Slew axis is set to ' + str(Az_response[-1]))
    
    controller.write('H')
    


def read_step_settings():
    
    controller.write('H')
    controller.write('S')
    
    J_response = list(controller.query('J|<', delay = 0.101))
    J_integers = ''.join([str(itm) for itm in J_response[1:-2]])
    J_decimals = ''.join([str(itm) for itm in J_response[-2:]])
    print('step value is ' + J_integers + '.' + J_decimals + ' degrees')
    
    Ae_response = list(controller.query('Ae<', delay = 0.101))
    print('Step axis is set to ' + str(Ae_response[-1]))
    
    controller.write('H')




def read_parameters():
    #read_boundaries()
    #time.sleep(0.501)
    read_axis()




def load_parameters():
    
    controller.write('H')
    controller.write('L')
    
    
    # the following sets the boundaries
    controller.write('Pas17000<')
    time.sleep(0.101)
    controller.write('Pab18000<')
    time.sleep(0.101)
    controller.write('Pes06000<')
    time.sleep(0.101)
    controller.write('Peb06500<')
    time.sleep(0.101)
    controller.write('Pat00500<')
    time.sleep(0.101)
    controller.write('Pet00500<')
    time.sleep(0.101)
    
    # the following makes sure the controller is set to Raster mode
    controller.write('M|R')
    time.sleep(0.101)
    # note: this sets raster scan A, as opposed to raster scan B
    # what this means I wont know without the operations manual
    
    # the following is setting the axis'
    controller.write('Aa1<')
    time.sleep(0.101)
    controller.write('Ae2<')
    time.sleep(0.101)
    controller.write('Az4<')
    time.sleep(0.101)
    
    controller.write('H')


def clear_device():
    
    controller.write('H')
    controller.write('L')
    
    controller.write('DCL<')
    
    #controller.read_stb()
    
    controller.write('H')


#clear_device()

#time.sleep(3.501)

# read_parameters()

load_parameters()

#time.sleep(3.501)

read_parameters()

#read_step_settings()

time.sleep(0.101)

# read_axis()

time.sleep(0.101)
controller.write('H')

#time.sleep(3.101)

#controller.write('G')

#time.sleep(20)

controller.write('H')

controller.close()
