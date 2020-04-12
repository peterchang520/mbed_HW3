import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 10.0
Ts = 1.0/Fs

t = np.arange(0,10,Ts)
x = np.arange(0,10,Ts)
y = np.arange(0,10,Ts)
z = np.arange(0,10,Ts)
tilt = np.arange(0,10,Ts)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)

for i in range(0, 10*int(Fs)):
    x[i] = float(s.readline())
for i in range(0, 10*int(Fs)):
    y[i] = float(s.readline())
for i in range(0, 10*int(Fs)):
    z[i] = float(s.readline())
for i in range(0, 10*int(Fs)):
    tilt[i] = int(s.readline())

fig, ax = plt.subplots(2,1)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('ACC Vector')
p1, = ax[0].plot(t, x)
p2, = ax[0].plot(t, y)
p3, = ax[0].plot(t, z)
ax[0].legend([p1, p2, p3], ['x', 'y', 'z'], loc='lower left')

ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
ax[1].scatter(t, tilt)

plt.show()
s.close()