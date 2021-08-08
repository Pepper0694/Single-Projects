#Shutdown script

import os
import time

shutdown = input('Do you wish to shutdown your computer? (yes/no or y/n)>')

shutdown = shutdown.strip().lower()


if shutdown not in ['yes', 'y']:
    exit()
else:
    wait = input('How long do you want to wait to shutdown?\n'
                 +'Input must be in minutes.   >')
    pause = str(int(wait)*60)
    os.system('shutdown -s -t '+pause)
    
    
