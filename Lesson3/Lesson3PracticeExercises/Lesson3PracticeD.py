# Selects all the park and ride facilities in a given city and saves them out to a new feature class. You can test with the city of 'Federal Way'.

import arcpy
arcpy.env.workspace = "C:\\Geog485\\Lesson3\\Lesson3PracticeExercises\\Lesson3PracticeExerciseD\\Washington.gdb\\"
arcpy.env.overwriteOutput = True

cityBoundaries = "CityBoundaries"
parkAndRide = "ParkAndRide"
outfc = "FederalWayParkAndRide"
selectedCity = "Federal Way"

try:
    # Create a query string for the parking capacity
    queryString = '"NAME" = ' + "'" + selectedCity + "'"
    
    # Make a feature layer with all the citys in Washington
    arcpy.MakeFeatureLayer_management(cityBoundaries, "SelectedCityLayer", queryString)

    # Make a feature layer with all the parks and rides in Washington
    arcpy.MakeFeatureLayer_management(parkAndRide, "ParkAndRideLayer")

    # Apply a selection to the ParkAndRideLayer (only select parks and rides contained by the current city)
    arcpy.SelectLayerByLocation_management("ParkAndRideLayer","CONTAINED_BY","SelectedCityLayer")

    # Use CopyFeatures to create a new feature class from the selected data
    arcpy.CopyFeatures_management("ParkAndRideLayer", outfc)

except:
    print "Could not complete the data processing"

finally:
    # Delete the feature layers even if there is an exception (error) raised
    arcpy.Delete_management("ParkAndRideLayer")
    arcpy.Delete_management("SelectedCityLayer")
