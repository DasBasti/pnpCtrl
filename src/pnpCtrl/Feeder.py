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

import machine

class Feeder(object):
    '''
    Feeder for Components
    '''

    def __init__(self, number, component, footprint, mech, x, y, z, phy):
        '''
        Initialize the feeder
        '''
        self.number = number
        self.component = component
        self.footprint = footprint
        self.x = x
        self.y = y
        self.z = z
        self.sourceType = mech
        self.phySizes = phy
        
    def contains(self, component, footprint):
        '''
        Whether it contains the components with given footprint
        '''
        if(self.component == component and self.footprint == footprint):
            return True
        return False
    
    def getNumber(self):
        return self.number
    
    def GCodeGrabNextComponent(self):
        '''
        Generate the GCode to grab the next component from the feeder.
        
        TODO: implement something for trays
        ''' 
        machine.gcode.moveToSaveHight()
        # move to the point of the belt hole
        machine.gcode.addMoveToBuffer(x = self.x+self.phySizes['P2'], 
                                      y = self.y+self.phySizes['F']) 
        # move the head down
        machine.gcode.addMoveToBuffer(z = self.z-self.phySizes['T2'])
        # advance the strip 
        machine.gcode.addMoveToBuffer(x = self.x+self.phySizes['P1'])
        # raise head
        machine.gcode.addMoveToBuffer(z = self.z+self.phySizes['T2'])
        # goto component
        machine.gcode.addMoveToBuffer(x = self.x, 
                                      y = self.y)
        # lower head
        machine.gcode.addMoveToBuffer(z = self.z-self.phySizes['T2'])
        # pick part
        machine.gcode.pick()
        # raise head
        machine.gcode.moveToSaveHight()
        
    def getComponentHeightOffset(self):
        '''
        Returns the offset created by picking a component
        '''
        return self.phySizes['t']   
        