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

import argparse
from pnpCtrl.JobFile import JobFile
import settings

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Process KiCad .pos file into g-code for pnpuCtrl(grbl fork).')

    parser.add_argument('-s', action='store_true', help='generate settings header for g-code file')
    parser.add_argument('-f', metavar='feeder.csv', help='feeder configuration')
    parser.add_argument('filename', metavar='kicad.pos', type=str, help='a KiCad generated position file')
    args = parser.parse_args()
    
    # print out settings if given the switch -s
    if (args.s):
        for item in settings.uCtrlSettings.items():
            print "$"+item[0]+"="+str(item[1])
    
    job = JobFile(args.filename)
    job.parseJobFile()
    job.optimizeJob()
    job.runJob()
    
    pass