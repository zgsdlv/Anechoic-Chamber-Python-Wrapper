# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 14:09:14 2025

@author: leviresearch
"""

'''
import pyvisa


rm = pyvisa.ResourceManager()

print(rm.list_resources())

'''

'''
instrument = rm.open_resource('GPIB0::3::INSTR')

print(instrument.query('*IDN?'))

instrument.read_termination

instrument.read_termination = '\r\n'
instrument.write_termination = '\r\n' # this is specific to this controller
instrument.baud_rate = 9600 # if i< gives S001, but if i< gives S003, = 2400

sesh = instrument.session

import time

instrument.write('FT1<')
instrument.write('CR')
instrument.write('LF')

time.sleep(0.11)

print(instrument.read_stb())

# read_stb gets the status byte, highly important. Keeps giving me 84 though

'''
import time

#print(instrument.query('Pas<', delay = 0.101))
Pas_response = list(instrument.query('Pas<', delay = 0.101))
Pas_integers = ''.join([str(itm) for itm in Pas_response[1:-2]])
Pas_decimals = ''.join([str(itm) for itm in Pas_response[-2:]])
print('Starting position of raster scan is ' + Pas_integers + '.' + Pas_decimals + ' degrees')

time.sleep(0.101)

#print(instrument.query('Pab<', delay = 0.101))
Pab_response = list(instrument.query('Pab<', delay = 0.101))
Pab_integers = ''.join([str(itm) for itm in Pab_response[1:-2]])
Pab_decimals = ''.join([str(itm) for itm in Pab_response[-2:]])
print('Ending position of raster scan is ' + Pab_integers + '.' + Pab_decimals + ' degrees')


