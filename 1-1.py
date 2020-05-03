import numpy as np
import matplotlib.pyplot as plt

import random

t_length = 1.0 #音の長さ[s]
sampling_f = 8000 #サンプリング周波数[Hz]

t = np.arange(0, t_length, 1/sampling_f)

noise = np.array([])
for i in range(0, int(t_length*sampling_f)):
    noise = np.append(noise, random.random()-0.5)


a = 0.5
f1 = 129.19921875*2
f2 = 129.19921875*4

#正弦波
y1 = np.sin(2*np.pi*f1*t) + 2*np.sin(2*np.pi*2*f2*t)

#ノイズ
#y1 = noise

#ノコギリ波
#y1 = (t*sampling_f)%100

#パルス波
#y1 = np.round((t*sampling_f/30)%1)


r = np.arange(200)
plt.plot(t[r], y1[r])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

input()
