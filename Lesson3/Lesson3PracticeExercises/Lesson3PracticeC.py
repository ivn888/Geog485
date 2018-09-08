# Select all park and ride facilities with a capacity of more than 500 parking spaces and put them into their own feature class. 
# The capacity of each park and ride is stored in the "Approx_Par" field.

import arcpy
arcpy.env.overwriteOutput = True

parkAndRideIn = "C:\\Geog485\\Lesson3\\Lesson3PracticeExercises\\Lesson3PracticeExerciseC\\Washington.gdb\\ParkAndRide"
parkAndRideOut = "C:\\Geog485\\Lesson3\\Lesson3PracticeExercises\\Lesson3PracticeExerciseC\\Washington.gdb\\ParkAndRideGreatThan500"
parkingCapacity = 500

# Create a query string for the parking capacity
queryString = '"Approx_Par" > ' + str(parkingCapacity)

try:
    # Make a feature layer for the current city
    arcpy.MakeFeatureLayer_management(parkAndRideIn, "ParkAndRideLayer", queryString)
    arcpy.CopyFeatures_management("ParkAndRideLayer", parkAndRideOut)

except:
    print "The parking capacity selection could not be completed."

finally:
    # Delete the ParkAndRideLayer
    arcpy.Delete_management("ParkAndRideLayer")
