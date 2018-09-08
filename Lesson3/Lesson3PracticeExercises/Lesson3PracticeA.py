# Find which cities contain park and ride facilities and what percentage of cities have at least one facility.
# Also calculate the percentage of cities that have a park and ride facility and print this figure for the user.

import arcpy
arcpy.env.overwriteOutput = True

cityBoundaries = "C:\\Geog485\\Lesson3\\Lesson3PracticeExercises\\Lesson3PracticeExerciseA\\Washington.gdb\\CityBoundaries"
parkAndRide = "C:\\Geog485\\Lesson3\\Lesson3PracticeExercises\\Lesson3PracticeExerciseA\\Washington.gdb\\ParkAndRide"
parkAndRideField = "HasParkAndRide"
citiesWithParkAndRide = 0

try:
    # Make a feature layer with all the citys in Washington
    arcpy.MakeFeatureLayer_management(cityBoundaries, "CitiesLayer")

    # Make a feature layer with all the parks and rides in Washington
    arcpy.MakeFeatureLayer_management(parkAndRide, "ParkAndRideLayer")

except:
    print "Could not create feature layers"

try:
    # Apply a selection to the CitiesLayer (only select cities that have parks and rides)
    arcpy.SelectLayerByLocation_management("CitiesLayer","CONTAINS","ParkAndRideLayer")

    # Create an update cursor and loop through each record, setting the HasParkAndRide field to "True."
    count = 0
    with arcpy.da.UpdateCursor("CitiesLayer", (parkAndRideField,)) as cursor:
        for row in cursor:
            row[0] = "True"
            cursor.updateRow(row)
            citiesWithParkAndRide += 1

# Delete the feature layers even if there is an exception (error) raised
finally:
    arcpy.Delete_management("ParkAndRideLayer")
    arcpy.Delete_management("CitiesLayer")

# Count the total number of cities
numCitiesCount = arcpy.GetCount_management(cityBoundaries)
numCities = int(numCitiesCount.getOutput(0))

# Calculate the percentage and print it for the user
percentCitiesWithParkAndRide = ((1.0 * citiesWithParkAndRide) / numCities) * 100

print str(percentCitiesWithParkAndRide) + "% of the cities have a park and ride facility."