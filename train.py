import sys
from time import sleep, time

sys.path.append('./pslab-python/build/lib')

from PSL import sciencelab

I = sciencelab.connect()

duty_cycle = 50
cycles = 20

start_time = time()
try:
    while cycles > 0:
        I.sqrPWM(freq=10000, 
                 h0=1e-3, p0=0, 
                 h1=duty_cycle / 100.0, p1=0, 
                 h2=1e-3, p2=0, 
                 h3=1e-3, p3=0)
        sleep(2)
        I.set_state(SQR2=0)
        sleep(2)
        cycles -= 1
finally:
    I.set_state(SQR2=0)

stop_time = time()
print('Time: {:.1f}s'.format(stop_time - start_time))
