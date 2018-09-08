# This script uses the Contour tool in the Spatial Analyst
# toolbox to create contour lines for the Fox Lake Quadrangle.
# The contour intervals are 25 meters and the base contour is 0.

import arcpy
from arcpy.sa import *

# Specify the input raster
inRaster = "C:/Geog485/Lesson1/foxlake"

# Set local variables
contourInterval = 25
baseContour = 0
outContours = "C:/Geog485/Lesson1/Project1/outcontours.shp"

# Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Execute Contour
try:
    Contour(inRaster, outContours, contourInterval, baseContour)
except:
    outContours = "C:/Geog485/Lesson1/Project1/outcontours1.shp"
    Contour(inRaster, outContours, contourInterval, baseContour)

# Check in the Spatial Analyst extension now that you're done
arcpy.CheckInExtension("Spatial")






