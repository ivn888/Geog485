# Reads the MysteryStatePoints.txt file and creates a state boundary polygon out of the coordinates.

import arcpy
import csv
arcpy.env.workspace = "C:\\Geog485\\Lesson4\\Lesson4PracticeExercises\\Lesson4PracticeExerciseA\\"

# Set up input and output variables for the script
statePoints = open("C:\\Geog485\\Lesson4\\Lesson4PracticeExercises\\Lesson4PracticeExerciseA\\data\\MysteryStatePoints.txt", "r")
polygonFC = "data\\MysteryState.shp"
spatialRef = arcpy.Describe(polygonFC).spatialReference

# Set up CSV reader
csvReader = csv.reader(statePoints)

# Make a new empty array
array = arcpy.Array()

try:
    # Loop through the lines in the file and get each coordinate
    for row in csvReader:
        lon = row[0]
        lat = row[1]
    
        # Make a point from the coordinate and add it to the array
        vertex = arcpy.Point(lon,lat)
        array.add(vertex)

    # Write the array to the feature class as a polygon feature
    with arcpy.da.InsertCursor(polygonFC, ("SHAPE@",)) as cursor:
        polygon = arcpy.Polygon(array, spatialRef)
        cursor.insertRow((polygon,))

except:
    print "Could not complete the data processing"