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

from pnpCtrl.Component import Component
import machine, re
import settings

class JobFile(object):
    '''
    This file contains the job information. For now it only uses the .pos file generated with KiCad
    '''
    components=list()


    def __init__(self, filename):
        '''
        Load a file name that has been created 
        '''
        print ";Load",filename
        with open(filename, 'r') as data:
            self.source = data.readlines()
            
            
    def parseJobFile(self):
        '''
        Go through the job and parse its tasks
        '''
        for line in self.source:
            if (line.startswith("###")):
                #print "ignore comment"
                pass
            elif (line.startswith('##')):
                try: # try to find the line saying it is in mm
                    match = re.search('Unit = (.+?),', line).group(1)
                except AttributeError:
                    match = None
                if (match == "mm"):
                    machine.gcode.addRawToBuffer("G21")
            elif (line.startswith('#')):
                #print ignore header line
                pass
            else:
                # delete empty fields
                item = filter(None, line.split(' '))
                # find feeder number by component and footprint
                feeder = machine.rack.findFeeder(item[1], item[2])
                if (feeder != None):
                    self.components.append( Component( name = item[0],
                                                       feeder = feeder,
                                                       x = float(item[3]),
                                                       y = float(item[4]),
                                                       r = float(item[5])
                                                       ))
                else:
                    print ";ignoring",item[0],item[1],item[2],"no feeder found"
                    pass
        print ";",len(self.components),"parts loaded"
        pass
     
    def runJob(self):
        ''' 
        Run job file consecutively
        '''             
        for component in self.components:
            #print "placing:", component.name
            # grab part
            machine.rack.getFeederByNumber(component.feeder).GCodeGrabNextComponent()
            # move to placing coordinate
            machine.gcode.addMoveToBuffer(x = component.x+settings.pcb_x_offset, 
                                          y = component.y+settings.pcb_y_offset)
            # rotate part
            # TODO: next axis if (component.r != 0): machine.gcode.rotate(component.r)
            # move down to board-level
            machine.gcode.addMoveToBuffer(z= machine.rack.getFeederByNumber(component.feeder).getComponentHeightOffset()
                                             +settings.pcb_z_offset)
            # place part
            machine.gcode.place()
            
                    
    def optimizeJob(self):
        '''
        TODO: run optimization for moves in execution list
        '''