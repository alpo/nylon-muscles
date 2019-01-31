import sys
from time import sleep, time

sys.path.append('./pslab-python/build/lib')

from PSL import sciencelab

I = sciencelab.connect()

motor_duty_cycle = 50
turns = 200
pulses_per_turn = 220

start_time = time()
try:
    I.sqr1(freq=10000, duty_cycle=motor_duty_cycle)
    I.countPulses(channel='SEN')
    count = 0
    while count < turns * pulses_per_turn:
        count = I.readPulseCount()
        sleep(0.02)
finally:
    I.set_state(SQR1=0)

stop_time = time()
print('Time: {:.1f}s, count {}'.format(time() - start_time, count))
