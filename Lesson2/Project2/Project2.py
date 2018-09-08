# Reprojects all datasets within a folder to a target projection given by another dataset

# Import system modules
import arcpy
from arcpy import env

try:
    # # Get the input parameters
    sourceWorkspace = arcpy.GetParameterAsText(0)
    targetProjectionDataset = arcpy.GetParameterAsText(1)
    env.workspace = sourceWorkspace
    # Get a list of the feature classes in the source folder
    fcList = arcpy.ListFeatureClasses()
    # Get target dataset's projection
    outCoordinateSystem = arcpy.Describe(targetProjectionDataset).spatialReference
    # Loop through the features in the folder
    for featureClass in fcList:
        inCoordinateSystem = arcpy.Describe(featureClass).spatialReference
        # Only reproject if the coordinate systems are not the same
        if inCoordinateSystem != outCoordinateSystem:
            # Get feature class name without shapefile extension
            featureClassName = featureClass.replace(".shp", "")
            outFeatureClass = sourceWorkspace + "\\" + featureClassName + "_projected.shp"
            # Execute Reprojection
            arcpy.Project_management(featureClass, outFeatureClass, outCoordinateSystem)
            arcpy.AddMessage("Reprojected file " + outFeatureClass)
            print "Reprojected file " + outFeatureClass

except:
    # Report if there was an error
    arcpy.AddError("Could not reproject feature classes")
    print "Could not reproject feature classes"
    print arcpy.GetMessages()
