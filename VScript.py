
# coding: utf-8

# In[1]:

#----------VERSION HISTORY-----------------------------------
# Feb 22, 2016 - Created Initial file, got file to ingest into code (v0.1->v0.1.1), working to figure out
# pulling an example variable out and plotting it (for testing purposes)  -Trent S.
#
# Mar 19, 2016 - Altered code to plot a single output variable, future work will go into adding more plots,
# figuring out what else needs to be added. Also changed into new git repository, went from Python 2.7 to
# 3.5 (v0.1.1->v1.0)
#------------------------------------------------------------------------------------------------------------------
print("\n Research Visualization Script v1.0 \n Author: Trent Spencer, Texas A&M University \n Python 3.5 \n See LICENSE for details of use \n See Github or Code for Version History \n")
# This section imports the necessary modules
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
from datetime import datetime

# Begin of actual script
def Vis_script(time, ni, nj, nk):
    data = nc.Dataset("../cm1out.nc")
    timedata = data.variables["time"][time]
    mxvertvort = data.variables['svs'][time, ni, nj]
    x = data.variables['xh'][ni]
    y = data.variables['yh'][nj]
    xall, yall = np.meshgrid(x, y)
    fig1 = plt.figure(figsize = (20,20))
    ax1 = fig1.add_subplot(111)
    return ax1.contourf(xall,yall,mxvertvort, cmap = cm.Blues)
    

print('Script began at:', datetime.utcnow(), 'UTC.')
sttime = time.time()
for t in range(0,3):
    Vis_script(t,range(0,120),range(0,120),0)
    plt.savefig(str(t) + "cm1svs.png")
entime = time.time()
print("Script took ", (entime - sttime), " seconds to run.")


# In[ ]:



