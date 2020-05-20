# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:46:15 2020

@author: caleb
"""
#x1 is distance in miles to fire from fire station
x1 = 2
#x2 is distance in miles to fire from fire hydrant
x2 = 1
#output is how many gallons of water per minute the hose is outputing
output = 183.9417491

#t1 and t2 are derived from the data given and the units are minutes
t1 = x1 * 60 / 35 + 6.5
t2 = 2 * x2 * 60 / 35 + 6.75
t3 = x1 * 60 / 45 + (900/output)
#total_gallons_first_hour is the total amount of gallons in the first hour and units are gallons
#if the tender is close enough to the fire hydrant that it gets back before the fire engine
#has used the water currently in the pool at t2 + t1, the last equation is used. If the
#time to use 2700 gallons is always slower than the tender return time the second equation
#is used.

if ((2700 / output) > (t2 + 4.5)):
    total_gallons_first_hour = ((60-(t3 + (2700/output)))/(2700/output) * 2700) + 3600
else:
    total_gallons_first_hour = ((60-(2 * t2 + t1 + 4.5 + (2700/output)))/(t2 + 4.5) * 2700) + 9000

#gph0 is the number of gallons in the first hour after the initial arrival time of the first truck
gph0 = (((60 + (x1 / 45 * 60))-(t2 + t1 + (2700/output)))/(t2 + 4.5) * 2700) + 6300
#gpm is the gallons per minute of the first hour
gpm = total_gallons_first_hour / 60
#gpm0 is the gallons per minute of the first hour after the initial arrival time of the first truck
gpm0 = gph0 / 60
stablized_output = (1 / (t2 + 4.5)) * 2700
print(total_gallons_first_hour,gpm,(t2 + t1),(t3 + (2700) / output),stablized_output,t2+4.5,2700/output)
