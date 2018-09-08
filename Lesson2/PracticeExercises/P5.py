# Clips feature classes in USA geodatabase to Iowa state boundary

# Import system modules
import arcpy
from arcpy import env

# Create path variables
sourceWorkspace = "C:\Geog485\Lesson2\Lesson2PracticeExercise\USA.gdb"
targetWorkspace = "C:\Geog485\Lesson2\Lesson2PracticeExercise\Iowa.gdb"
clipFeature = "C:\Geog485\Lesson2\Lesson2PracticeExercise\Iowa.gdb\Iowa"

env.workspace = sourceWorkspace
fcList = arcpy.ListFeatureClasses()

try:
    # Loop through the features in the USA gdb
    for featureClass in fcList:
        outClipFeatureClass = targetWorkspace + "\Iowa" + featureClass
        # Execute Clip
        arcpy.Clip_analysis(featureClass, clipFeature, outClipFeatureClass)
        arcpy.AddMessage("Wrote clipped file " + outClipFeatureClass + ". ")
        print "Wrote clipped file " + outClipFeatureClass + ". "

except:
    # Report if there was an error
    arcpy.AddError("Could not clip feature classes")
    print "Could not clip feature classes"
    print arcpy.GetMessages()

