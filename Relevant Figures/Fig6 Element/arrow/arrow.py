#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:51:05 2024

@author: aliciaglenda
"""

import matplotlib.patches as mpatches

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from qutip import *
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from collections import Counter
from matplotlib import cm
from matplotlib import colors  
import seaborn as sns  
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.image as mpimg

from matplotlib import colors  
from matplotlib import rc


fig, ax = plt.subplots(figsize=(3, 3))
xarr = mpatches.FancyArrowPatch((0.5, 0.5), (2, 0.5),
                               arrowstyle='->,head_width=.7', mutation_scale=10,color='k')
yarr = mpatches.FancyArrowPatch((0.5, 0.5), (0.5, 2),
                               arrowstyle='->,head_width=.7', mutation_scale=10,color='k')
ax.add_patch(xarr)
ax.add_patch(yarr)
ax.set(xlim=(0, 2), ylim=(0, 2))