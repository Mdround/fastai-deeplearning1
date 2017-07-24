### MDR, June 2017 ### 
### utilities for deep learning work ###

import os

def set_gpu_fan_speed(speed = 0):
    """Puts the GPU fans into manual mode, and sets the speed to parameter value.
    N.B. Setting to any speed <80 will switch to automatic mode.
    ... and anything >= 100 is held to 100."""
    
    speed = int(speed)
    if speed > 100: speed = 100
    if speed >= 80:
        ## Turn the GPU fans up...
        speed = str(speed)
        man_comd = 'nvidia-settings -a [gpu:0]/GPUFanControlState=1'
        fan_comd = ' -a [fan:0]/GPUTargetFanSpeed=' + speed + ' -c :0.0'
        os.system(man_comd + fan_comd)
    else:
        ##turn the fans back to auto
        os.system('nvidia-settings -a [gpu:0]/GPUFanControlState=0')
    return;
