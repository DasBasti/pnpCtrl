'''

 pnpCtrl - a pick and place g-code generator
 
 Copyright (c) 2015 Bastian Neumann - info@kurzschluss-blog.de
 
 pnpCtrl is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 pnpCtrl is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRENTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with pnpCtrl. If not, see <http://www.gnu.org/licenses/>

'''

# Maximum feed rates in mm/min
machine_x_max_feed_rate = 25000.000
machine_y_max_feed_rate = 25000.000
machine_z_max_feed_rate = 25000.000

# Maximum operation range in mm
machine_x_max_travel = 500.000
machine_y_max_travel = 500.000
machine_z_max_travel = 25.000

# PCB offset in mm
pcb_x_offset = 50.000
pcb_y_offset = 50.000
pcb_z_offset = 2.500



# Space left for head to move above the feeder
feeder_z_offset = 0.1

# GCode generation Values
gcode_normal_move = "G1"
gcode_vacuum_on = "M8"
gcode_vacuum_off = "M9"
gcode_vacuum_dwell = 0.1 # s to wait for suction


uCtrlSettings = dict()
uCtrlSettings['0'] = 5            #(step pulse, usec)
uCtrlSettings['1'] = 5            #(step idle delay, msec)
uCtrlSettings['2'] = 0            #(step port invert mask:00000000)
uCtrlSettings['3'] = 6            #(dir port invert mask:00000110)
uCtrlSettings['4'] = 0            #(step enable invert, bool)
uCtrlSettings['5'] = 0            #(limit pins invert, bool)
uCtrlSettings['6'] = 0            #(probe pin invert, bool)
uCtrlSettings['10'] = 3           #(status report mask:00000011)
uCtrlSettings['11'] = 0.020       #(junction deviation, mm)
uCtrlSettings['12'] = 0.002       #(arc tolerance, mm)
uCtrlSettings['13'] = 0           #(report inches, bool)
uCtrlSettings['14'] = 1           #(auto start, bool)
uCtrlSettings['20'] = 0           #(soft limits, bool)
uCtrlSettings['21'] = 0           #(hard limits, bool)
uCtrlSettings['22'] = 1           #(homing cycle, bool)
uCtrlSettings['23'] = 0           #(homing dir invert mask:00000000)
uCtrlSettings['24'] = 5000.000    #(homing feed, mm/min)
uCtrlSettings['25'] = 5000.000    #(homing seek, mm/min)
uCtrlSettings['26'] = 136         #(homing debounce, msec)
uCtrlSettings['27'] = 1.000       #(homing pull-off, mm)
uCtrlSettings['100'] = 80.000    #(x, step/mm) 20 tooth gt2 pulley -> 40mm/rot
uCtrlSettings['101'] = 80.000    #(y, step/mm) 200step /rot -> 3200 ustep/rot
uCtrlSettings['102'] = 80.000    #(z, step/mm) --> 80 step/mm
uCtrlSettings['103'] = 8.889     #(a, step/mm) 3200/630 -> 8.8888888 usteps/degree 
uCtrlSettings['110'] = 60000.000   #(x max rate, mm/min) 60000 = 1m/s
uCtrlSettings['111'] = 60000.000   #(y max rate, mm/min)
uCtrlSettings['112'] = 60000.000   #(z max rate, mm/min)
uCtrlSettings['113'] = 60000.000  #( max rate, mm/min)
uCtrlSettings['120'] = 250.000     #(x accel, mm/sec^2)
uCtrlSettings['121'] = 250.000     #(y accel, mm/sec^2)
uCtrlSettings['122'] = 250.000     #(z accel, mm/sec^2)
uCtrlSettings['123'] = 250.000     #( accel, mm/sec^2)
uCtrlSettings['130'] = machine_x_max_travel    #(x max travel, mm)
uCtrlSettings['131'] = machine_y_max_travel    #(y max travel, mm)
uCtrlSettings['132'] = machine_z_max_travel    #(z max travel, mm)
uCtrlSettings['133'] = 0.000     #( max travel, mm)


    