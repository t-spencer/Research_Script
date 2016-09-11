
# coding: utf-8

# In[ ]:

#----------VERSION HISTORY-----------------------------------
# Feb 22, 2016 - Created Initial file, got file to ingest into code (v0.1->v0.1.1), working to figure out
# pulling an example variable out and plotting it (for testing purposes)  -Trent S.

# Mar 19, 2016 - Altered code to plot a single output variable, future work will go into adding more plots,
# figuring out what else needs to be added. Also changed into new git repository, went from Python 2.7 to
# 3.5 (v0.1.1->v1.0)

# Mar 20, 2016 - Added code to create second plot, seems to work fine. Added comments for each line for
# anybody who would like to use this in the future. Not too many other changes, upcoming work may include
# creating reflectivity color table, then plotting. (v1.0->v1.0.1)

# Mar 22, 2016 - Completely redid code, moved to class structure instead of one long definition. Will go back
# and insert comments on lines again for whoever looks at this in the future. Having issues with the plots of 
# the Composite Reflectivity and the Cold pool. Maybe need a new model run? More work this week on this issue,
# will log in github issue tracker. (v1.0.1->v2.0)
#------------------------------------------------------------------------------------------------------------------

# Prints opening info
print("\n Research Visualization Script v2.0 \n Author: Trent Spencer, Texas A&M University \n Python 3.5 \n See LICENSE for details of use \n See Github or Code for Version History \n")

# This section imports the necessary modules
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
from datetime import datetime
from metpy.plots import ctables

# Begin of actual script
class ResPlot:
    def __init__(self, filename):
        self.filename = filename
        self.to_plot = []
        self.ni = 0
        self.nj = 0
        self.nk = 0
        self.time = 0
        
    def getinfo(self):
        self.ni = int(input("Enter ni value from namelist: "))
        self.nj = int(input("Enter nj value from namelist: "))
        self.nk = int(input("Enter nk value from namelist: "))
        self.time = int(input("Enter time value from ncdump: "))
    
    def whatplot(self):
        names = ['Cold Pool Intensity', 'Cold Pool Height', 'Max Updraft Helicity', 'Reflectivity', 'max vert vorticity at lowest level', 'surface potential temperature', 'maximum updraft speed at 5 km AGL']
        v = ['cpc','cph','shs','cref','svs','sfcth','sus']
        validanswers = ['Y','y','Yes','yes', 'YES', "Sure", 'sure', 'OK', 'ok']
        b = 0
        for vari in names:
            a = input("Plot " + vari + '? ')
            if a in validanswers:
                self.to_plot.append(v[b])
                b = b + 1
            else:
                b = b + 1
    
    def plot(self):
        '''Does all the plotting'''
        data = nc.Dataset(self.filename)
        x = data['xh'][range(self.ni)]
        y = data['yh'][range(self.nj)]
        xall, yall = np.meshgrid(x,y)
        if 'cpc' in self.to_plot:
            for t in range(self.time):
                fig1 = plt.figure(figsize = (25,25) )
                cpcdata = data['cpc'][t, range(self.nj), range(self.ni)]
                ax1 = fig1.add_subplot(111)
                ax1.contourf(xall, yall, cpcdata, cmap = cm.Blues)
                ax1.set_title(str(data['time'][t]), fontsize = 30)
                plt.savefig("cpc_" + str(t))
                plt.close('all')
                
        if 'cph' in self.to_plot:
            for t in range(self.time):
                fig1 = plt.figure(figsize = (25,25) )
                cpcdata = data['cph'][t, range(self.nj), range(self.ni)]
                ax1 = fig1.add_subplot(111)
                ax1.contourf(xall, yall, cpcdata, cmap = cm.Blues)
                ax1.set_title(str(data['time'][t]), fontsize = 30)
                plt.savefig("cph_" + str(t))
                plt.close('all')
        
        if 'shs' in self.to_plot:
            for t in range(self.time):
                fig1 = plt.figure(figsize = (25,25) )
                shsdata = data['shs'][t, range(self.nj), range(self.ni)]
                ax1 = fig1.add_subplot(111)
                ax1.contourf(xall, yall, shsdata, cmap = cm.Blues)
                ax1.set_title(str(data['time'][t]), fontsize = 30)
                plt.savefig("shs_" + str(t))
                plt.close('all')

        if 'cref' in self.to_plot:
            for t in range(self.time):
                fig1 = plt.figure(figsize = (25,25) )
                crefdata = data['cref'][t, range(self.nj), range(self.ni)]
                ax1 = fig1.add_subplot(111)
                cmap = ctables.registry.get_colortable('NWSReflectivityExpanded')
                ax1.contourf(xall, yall, crefdata, cmap = cmap)
                ax1.set_title(str(data['time'][t]), fontsize = 30)
                plt.savefig("cref_" + str(t))
                plt.close('all')
                
        if 'svs' in self.to_plot:
            for t in range(self.time):
                fig1 = plt.figure(figsize = (25,25) )              
                svsdata = data['svs'][t, range(self.nj), range(self.ni)]
                ax1 = fig1.add_subplot(111)
                ax1.contourf(xall, yall, svsdata, cmap = cm.jet)
                ax1.set_title(str(data['time'][t]), fontsize = 30)
                plt.savefig("svs_" + str(t))
                plt.close('all')
                
        if 'sfcth' in self.to_plot:
            for t in range(self.time):
                fig1 = plt.figure(figsize = (25,25) )              
                thdata = data['th'][t, 0, range(self.nj), range(self.ni)]
                ax1 = fig1.add_subplot(111)
                ax1.contourf(xall, yall, thdata, cmap = cm.Blues)
                ax1.set_title(str(data['time'][t]), fontsize = 30)
                plt.savefig("sfcth_" + str(t))
                plt.close('all')

        if 'sus' in self.to_plot:
            for t in range(self.time):
                fig1 = plt.figure(figsize = (25,25) )                
                susdata = data['sus'][t, range(self.nj), range(self.ni)]
                ax1 = fig1.add_subplot(111)
                ax1.contourf(xall, yall, susdata, cmap = cm.Blues)
                ax1.set_title(str(data['time'][t]), fontsize = 30)
                plt.savefig("susth_" + str(t))
                plt.close('all')
                 
a = ResPlot('../cm1out.nc')
a.whatplot()
a.getinfo()
print('\n Script began at:', datetime.utcnow(), 'UTC.')
sttime = time.time()
a.plot()
entime = time.time()
if entime - sttime < 60:
    print("\n Script took ", (entime - sttime), " seconds to run. \n")
else:
    print("\n Script took ", (entime - sttime)/60 , " minutes to run. \n")

