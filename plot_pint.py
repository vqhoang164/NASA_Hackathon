# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:48:46 2022

@author: vqhoa
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

xline = [1,2,3]
yline = [1,2,3]
zline = [1,2,3]


ax.plot3D(xline, yline, zline, 'gray')

