from dronekit import *

vehicle = connect('udp:10.0.0.1', wait_ready=True)
