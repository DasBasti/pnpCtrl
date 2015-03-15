# pnpCtrl

This software is a pick and place g-code generator. It will read a KiCad .pos file, corelates feeder information with the parts and generates movement based on g-code.
The code is executable with [grbl](https://github.com/grbl/grbl).

planned features:
- automatic homing of pcb with fiducials.
- optical inspection and delta correction of picked part.
- optical inspection of placed part.
- feeding from trays.
