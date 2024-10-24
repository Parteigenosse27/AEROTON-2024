import serial
from serial import Serial
from pymavlink import mavutil
ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1)
print(ser)
mav = mavutil.mavlink_connection('/dev/ttyACM0')
mav.wait_heartbeat()
def set_motor_speeds(speeds):
    scaled_speeds = [int(speed * 1000) for speed in speeds]
    mav.mav.set_position_target_local_ned_send(0,
                                           mav.target_system,
                                           mav.target_component,
                                           mavutil.mavlink.MAV_FRAME_LOCAL_NED,
                                           0b0000111111111111,
                                           0, 0, 0,
                                           scaled_speeds[0],
                                           scaled_speeds[1], scaled_speeds[2], 
                                           scaled_speeds[3],
                                           0, 0, 0,
                                           0, 0)
set_motor_speeds([1.0, 1.0, 1.0, 1.0])
while True:
    msg = mav.recv_match(blocking=True)
    if msg:
        print(msg)
ser.close()