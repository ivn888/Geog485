# Create copies of a template shapefile

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "C:\Geog485\Lesson1"

# Set local variables
out_path = "C:\Geog485\Lesson2\PracticeExercises"
geometry_type = "POINT"
template = "Precip2008Readings.shp"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_reference = arcpy.Describe("Precip2008Readings.shp").spatialReference

for year in range(2009, 2013):
    out_name = "Precip" + str(year) + "Readings.shp"
    # Execute CreateFeatureclass
    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)
