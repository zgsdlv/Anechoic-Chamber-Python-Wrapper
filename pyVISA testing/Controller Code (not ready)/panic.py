# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 17:35:39 2025

@author: leviresearch
"""

'''
This script is designed as a panic button to stop alloperations of the
anechoic chamber, should something unexpected start to happen. This was
designed first so that all subsequent scripts that are made and tests that
are done can be stopped at a moments notice.

In order to test this script, the chamber should be oprated manually (via the
control panel), and then this script should be run to see if it halts all
operations.

Requirements of this script:
    - write a command to the controller to stop all movement and cancel
      all commands, and return the controller to a standby state
    - be able to stop the functions of all pyVISA scripts written for the
      controler. Likely will be done with os.system('taskkill /_______')
      - note: can do os.system('taskkill /f /_______') is a more forceful 
        kill method
      - note: on windows, there is no "killall", so in the event multiple
        scripts of the same name are running (somehow), then this script would
        need to be run multiple times
    - [optional] if the controller returns an error code that isnt good, then
      this script could also be triggered
'''

#DO NOT RUN THIS SCRIPT IT IS NOT READY TO BE USED

'''
import initialization

device = initialization.instrument

# this first halt is to make sure the movement is stopped immediately, even if
# some rogue scrit is gonna start it up again before they are ancelled by this
# script. A second one lies farther down
device.write('H')


in here, all the things that cancel other scripts should be


# this second halt is written in case any other script tried starting the
# chamber while the scripts were being cancelled.
# The reason for this redundancy is peace of mind since I am paranoid
device.write('H')
'''


