# Find which cities contain at least two park and ride facilities
# Also calculate the percentage of cities that have at least two park and ride facility and print this figure for the user.

import arcpy
arcpy.env.overwriteOutput = True

cityBoundaries = "C:\\Geog485\\Lesson3\\Lesson3PracticeExercises\\Lesson3PracticeExerciseB\\Washington.gdb\\CityBoundaries"
parkAndRide = "C:\\Geog485\\Lesson3\\Lesson3PracticeExercises\\Lesson3PracticeExerciseB\\Washington.gdb\\ParkAndRide"
cityIDStringField = "CI_FIPS"
parkAndRideField = "HasTwoParkAndRides"
citiesWithTwoParkAndRides = 0

# Make a feature layer with all the parks and rides in Washington
arcpy.MakeFeatureLayer_management(parkAndRide, "ParkAndRideLayer")

# Create an update cursor for the cities
with arcpy.da.UpdateCursor(cityBoundaries, (cityIDStringField, parkAndRideField,)) as cursor:
    for row in cursor:
        # Create a query string for the current city
        cityIDString = row[0]
        queryString = '"' + cityIDStringField + '" = ' + "'" + cityIDString + "'"

        # Make a feature layer for the current city
        arcpy.MakeFeatureLayer_management(cityBoundaries, "CurrentCityLayer", queryString)

        try:
            # Apply a selection to the ParkAndRideLayer (only select parks and rides contained by the current city)
            arcpy.SelectLayerByLocation_management("ParkAndRideLayer","CONTAINED_BY","CurrentCityLayer")
            # Count the number of parks and rides within the city
            parkAndRidesCount = arcpy.GetCount_management("ParkAndRideLayer")
            numSelectedParkAndRide = int(parkAndRidesCount.getOutput(0))

            # Update the value if the city has more than two parks and rides
            if numSelectedParkAndRide >= 2:
                row[1] = "True"
                cursor.updateRow(row)
                citiesWithTwoParkAndRides += 1
        finally:
            # Delete the CurrentCityLayer before starting next iteration
            arcpy.Delete_management("CurrentCityLayer")

# Delete the feature layers even if there is an exception (error) raised
arcpy.Delete_management("ParkAndRideLayer")

# Count the total number of cities
numCitiesCount = arcpy.GetCount_management(cityBoundaries)
numCities = int(numCitiesCount.getOutput(0))

# Calculate the percentage and print it for the user
percentCitiesWithParkAndRide = ((1.0 * citiesWithTwoParkAndRides) / numCities) * 100

print str(percentCitiesWithParkAndRide) + "% of the cities have two or more park and ride facilities."