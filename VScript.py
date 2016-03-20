
# coding: utf-8

# In[5]:

#----------VERSION HISTORY-----------------------------------
# Feb 22, 2016 - Created Initial file, got file to ingest into code (v0.1->v0.1.1), working to figure out
# pulling an example variable out and plotting it (for testing purposes)  -Trent S.

# Mar 19, 2016 - Altered code to plot a single output variable, future work will go into adding more plots,
# figuring out what else needs to be added. Also changed into new git repository, went from Python 2.7 to
# 3.5 (v0.1.1->v1.0)

# Mar 20, 2016 - Added code to create second plot, seems to work fine. Added comments for each line for
# anybody who would like to use this in the future. Not too many other changes, upcoming work may include
# creating reflectivity color table, then plotting. (v1.0->v1.0.1)
#------------------------------------------------------------------------------------------------------------------

# Prints opening info
print("\n Research Visualization Script v1.0.1 \n Author: Trent Spencer, Texas A&M University \n Python 3.5 \n See LICENSE for details of use \n See Github or Code for Version History \n")

# This section imports the necessary modules
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
from datetime import datetime

# Begin of actual script
def Vis_script(time, ni, nj, nk):
    '''This function pulls the data from the .nc file and returns the plotted images specified in the code.'''
    data = nc.Dataset("../cm1out.nc") # opens file 
    timedata = data.variables["time"][time] #pulls time
    mxheli = data.variables['shs'][time, nj, ni] # pulls max updraft helicity
    cold = data.variables['cph'][time, nj, ni] # pulls cold pool height
    x = data.variables['xh'][ni]   # pulls x-coordinates
    y = data.variables['yh'][nj]   # pulls y-coordinates
    xall, yall = np.meshgrid(x, y) # creates grid for plotting data
    fig1 = plt.figure(figsize = (25,25)) # creates figure
    ax1 = fig1.add_subplot(121) # creates first plot
    ax1.contourf(xall, yall, mxheli, cmap = cm.Blues) # makes filled contours in first plot displaying updraft helicity
    ax2 = fig1.add_subplot(122) # creates second plot
    ax2.contourf(xall, yall, cold, cmap = cm.Blues) # makes filled contours of cold pool height in second plot
    return fig1  # returns the figure
    

print('\n Script began at:', datetime.utcnow(), 'UTC.')
sttime = time.time()
for t in range(0,45): # loops over each time step
    Vis_script(t,range(0,200),range(0,200),range(0,40))
    plt.savefig(str(t) + "cm1svs.png") # saves images as .png (Change to .pdf?)
    plt.close('all') # closes open figure to keep memory usage low (~160 mb RAM as of 4/20/16)
entime = time.time()
print("Script took ", (entime - sttime), " seconds to run. \n")


# In[ ]:



