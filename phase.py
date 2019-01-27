import matplotlib.pyplot as plt
import numpy as np
Fs=70
f=1
sample = 1000
x= np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.subplot(311)
plt.plot(x,y)
Fs1=80
f=1
sample=1000
a=np.arange(sample)
b=np.sin(2*np.pi*f*a/Fs1+180)
plt.subplot(312)
plt.plot(a,b,'g')
z=y+b
plt.subplot(313)
plt.plot(a,z)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()

