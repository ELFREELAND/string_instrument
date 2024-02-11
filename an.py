from matplotlib import pyplot as plt
from matplotlib import animation as ani
import numpy as np
import scipy as sp

import pickle
import sys

if len(sys.argv) < 2:
    raise TypeError("Expected a file name, e.g. 'python an.py open.dat'")

fname = sys.argv[1]   

with open(fname, "rb") as f:
    s_har2 = pickle.load(f)

#find maximum displacement to set axis limits
yl = 1.05*np.max(np.abs(s_har2["y"][0:500,:]))

f, ax = plt.subplots()

xdata = np.linspace(0, 0.75, 500)

line = ax.plot(xdata, s_har2["y"][0:500,0])[0]
label = ax.annotate("", (0.8,0.9), xycoords="axes fraction")

ax.set_ylim(bottom=-yl, top=yl)
ax.grid(True)
ax.set_xlabel("Position, m")
ax.set_ylabel("Displacement, m")

def frame(index):
    line.set_data(xdata, s_har2["y"][0:500,index])
    label.set(text="t={0:.4f} s".format(s_har2["t"][index]))
    return line, label

anim = ani.FuncAnimation(f, frame, interval=100, save_count=10000)

plt.show()
