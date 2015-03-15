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

class Component(object):
    '''
    A Component does come with a lot of different informations
    '''


    def __init__(self, name, feeder=0, x=0, y=0, r=0):
        '''
        Constructor does need a name at least
        '''
        self.name = name
        self.feeder = feeder
        self.x = x
        self.y = y
        self.r = r
