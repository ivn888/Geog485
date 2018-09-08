import arcpy
import csv
arcpy.env.overwriteOutput = True

# Create an empty shapefile to store polylines
polyLineFC = "C:\\Geog485\\Lesson4\\Project4\\Data\\RhinoPaths.shp"
out_path = "C:\\Geog485\\Lesson4\\Project4\\Data"
out_name = "RhinoPaths.shp"
geometry_type = "POLYLINE"
sr = arcpy.SpatialReference(4326) # 4326 is the factory code for WGS 1984
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, spatial_reference=sr)
arcpy.AddField_management(polyLineFC, "NAME", "TEXT")

# Create an empty dictionary to store names of rhinos and their corresponding coordinates
rhinoDict = {}

# Open csv
rhinoFile = open("C:\\Geog485\\Lesson4\\Project4\\RhinoObservations.csv", "r")
csvReader = csv.reader(rhinoFile)

# Read header of csv
header = csvReader.next()

# Start loop through rest of csv
for row in csvReader:
    # Pull out lat, lon, name
    lon = row[1]
    lat = row[2]
    name = row[3]
    # Create a new point object using the lon and lat.
    point = arcpy.Point(lon,lat)
    # Determine if the dictionary has a key for the rhino name.
    if name not in rhinoDict:
        # If no key exists, create a new array object.
        array = arcpy.Array()
        # Add the point to the array.
        array.add(point)
        # Add the array to the dictionary using the rhino name as the key.
        rhinoDict[name] = array
    else:
        rhinoDict[name].add(point)

# Loop through each key of the dictionary
for k in rhinoDict:
    # Write the points to the feature class as a polygon feature with a name field
    with arcpy.da.InsertCursor(polyLineFC, ("SHAPE@","NAME",)) as cursor:
        polyline = arcpy.Polyline(rhinoDict[k])
        cursor.insertRow((polyline, k))