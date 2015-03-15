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

import settings

class GCodeStreamer(object):
    '''
    Class to coordinate GCode to the pnp machine
    '''
    buffer = list()


    def __init__(self):
        '''
        Contruct
        '''
        
        
    def addRawToBuffer(self, line):
        '''
        Add line of GCode to buffer
        '''
        print line
        self.buffer.append(line)
        
    def addMoveToBuffer(self, x=-1, y=-1, z=-1, speed=-1):
        '''
        Generate and add move code to buffer
        
        only positive values are accepted as valid coordinates
        '''
        line = list()
        # sanity check if we are in our accessible area
        if (x <= settings.machine_x_max_travel
            and y <= settings.machine_y_max_travel
            and z <= settings.machine_z_max_travel):
            
            line.append(settings.gcode_normal_move) # initialize move

            # loading the moving axis maximum speeds
            speeds = list()
            if (x != -1):
                speeds.append(settings.machine_x_max_feed_rate)
                line.append("X"+str(x))
            if (y != -1):
                speeds.append(settings.machine_x_max_feed_rate)
                line.append("Y"+str(y))
            if (z != -1):
                speeds.append(settings.machine_x_max_feed_rate)
                line.append("Z"+str(z))
            
            # use slowest max speed if given none            
            if (speed == -1):
                speed = min(speeds)
            else: # check if the given speed is ok
                if (speed > max(speeds)):
                    speed = max(speeds) # limit speed to max speed
                    print "move limited to maximum speed"
            
            line.append("F"+str(speed))
            
            self.addRawToBuffer(' '.join(line))
            
    def moveToSaveHight(self):
        '''
        Moves the Head to a save height to move above everything
        '''
        self.addMoveToBuffer(z=settings.machine_z_max_travel, speed=settings.machine_z_max_feed_rate)
        
    def pick(self):
        '''
        do whatever is neccessary to have the nozle stick to a component
        
        -activate vacuum
        -wait for suction
        '''
        self.addRawToBuffer(settings.gcode_vacuum_on) # vacuum on
        self.wait(settings.gcode_vacuum_dwell) # wait for suction to grab
        
    def place(self):
        '''
        do whatever is neccessary to have the nozle stick to a component
        
        -deactivate vaccum
        -wait for venting
        '''
        self.addRawToBuffer(settings.gcode_vacuum_off) # vacuum off
        self.wait(settings.gcode_vacuum_dwell) # wait for vacuum to be vented
        
    def wait(self, seconds):
        '''
        dwell at the current position for seconds
        '''
        self.addRawToBuffer("G4 P"+str(seconds))
        
    def rotate(self, degree):
        '''
        rotate the head for degree
        '''
        self.addRawToBuffer("G91") # set to relative moves rotation always starts at 0
        self.addRawToBuffer("G1 A"+str(degree))
        self.addRawToBuffer("G90") # set to absolute moves
        
        