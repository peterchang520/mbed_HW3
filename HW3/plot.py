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

plt.plot(t, x)
plt.plot(t, y)
plt.plot(t, z)
plt.plot(t, tilt)
plt.show()
s.close()