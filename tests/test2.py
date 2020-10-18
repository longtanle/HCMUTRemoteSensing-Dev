# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:25:04 2020

@author: tanlo
"""

import rasterio
import rasterio.plot
import pyproj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

date = '2020-05-12'

#filepath = 'https://storage.googleapis.com/gcp-public-data-landsat/LC08/01/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'
filepath5= "C:/landsat_data/data/LC08_L1TP_125052_20200122_20200128_01_T1_B5.TIF"
filepath4= "C:/landsat_data/data/LC08_L1TP_125052_20200122_20200128_01_T1_B4.TIF"
#url = 'https://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'
with rasterio.open(filepath4) as src:
    profile = src.profile
#    oviews = src.overviews(1) # list of overviews from biggest to smallest
#    oview = oviews[1]  # Use second-highest resolution overview
    red = src.read(1)
#    thumbnail = thumbnail.astype('f4')
#    thumbnail[thumbnail==0] = np.nan
    
print('array type: ',type(red))
print(np.amax(red))
print(np.amin(min))

plt.imshow(red)
plt.colorbar()
plt.title('Overview - Band 4 {}'.format(filepath4, red.shape))
plt.xlabel('Column #')
plt.ylabel('Row #')

with rasterio.open(filepath5) as src:
    profile = src.profile
#    oviews = src.overviews(1) # list of overviews from biggest to smallest
#    oview = oviews[1]  # Use second-highest resolution overview
    nir = src.read(1)
#    thumbnail = thumbnail.astype('f4')
#    thumbnail[thumbnail==0] = np.nan
    
print('array type: ',type(nir))
print(np.amax(nir))
print(np.amin(nir))

plt.imshow(red)
plt.colorbar()
plt.title('Overview - Band 5 {}'.format(filepath5, nir.shape))
plt.xlabel('Column #')
plt.ylabel('Row #')

def calc_ndvi(nir,red):
    '''Calculate NDVI from integer arrays'''
    nir = nir.astype('f4')
    red = red.astype('f4')
    ndvi = (nir - red) / (nir + red)
    return ndvi

ndvi = calc_ndvi(nir,red)

print(type(ndvi))
print(ndvi)
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar()
plt.title('NDVI {}'.format(date))
plt.xlabel('Column #')
plt.ylabel('Row #')