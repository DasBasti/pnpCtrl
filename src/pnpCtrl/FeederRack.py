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

import csv
from pnpCtrl.Feeder import Feeder

class FeederRack(object):
    '''
    Manages all the feeders in the machine
    '''
    feeders = list()


    def __init__(self):
        '''
        Construct feeder rack from feeder.csv
        '''
        with open('data/feeder.csv', 'rb') as csvfile:
            reader = csv.DictReader(filter(lambda row: row[0]!='#',csvfile), delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader: # load feeders into rack
                self.feeders.append( Feeder( row['number'], 
                                             row['component'], 
                                             row['footprint'], 
                                             row['type'], 
                                             row['x'], 
                                             row['y'], 
                                             row['z'],
                                             {k: row.get(k, None) for k in ('t','W','F','E','A0','B0','D0','P0','P1','P2','T2')} #subset the row for belt sizes
                                            ))
        
        
    def addFeeder(self, feeder):
        '''
        TODO: Add feeder to the list
        '''
        print "to be implemented"
        
        
    def findFeeder(self, component, footprint):
        '''
        Find the feeder number according to component name and footprint from pos file
        '''
        for feeder in self.feeders:
            if (feeder.contains(component, footprint)):
                return feeder.getNumber()
        return None
    
    def getFeederByNumber(self, number):
        for feeder in self.feeders:
            if (feeder.number == number):
                return feeder
        return None
        