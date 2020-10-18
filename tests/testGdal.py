# -*- coding: utf-8 -*-

import os
import math

from osgeo import gdal
from osgeo import gdal_array
import numpy as np

filepath= "/home/netfpga/Workspace/remoteSensing/landsatData/LC08_L1TP_124053_20200420_20200508_01_T1/NITK_RSGIS_20201015_145401/Outputs/LC8[124_53](2020-04-20_03-07)NDVI.TIF"

# Open the file:
raster = gdal.Open(filepath)
rasterArray = gdal_array.LoadFile(filepath)
# Check type of the variable 'raster'
type(raster)

# Projection
raster.GetProjection()

# Dimensions
print(raster.RasterXSize)
print(raster.RasterYSize)

# Number of bands
raster.RasterCount

# Metadata for the raster dataset
raster.GetMetadata()

# Read the raster band as separate variable
band = raster.GetRasterBand(1).ReadAsArray()

# Check type of the variable 'band'
print(np.amax(band))
# Data type of the values
#gdal.GetDataTypeName(band.DataType)

# Compute statistics if needed
#if band.GetMinimum() is None or band.GetMaximum()is None:
#    band.ComputeStatistics(0)
#    print("Statistics computed.")

# Fetch metadata for the band
#band.GetMetadata()

# Print only selected metadata:
#print ("[ NO DATA VALUE ] = ", band.GetNoDataValue()) # none
#print ("[ MIN ] = ", band.GetMinimum())
#print ("[ MAX ] = ", band.GetMaximum())