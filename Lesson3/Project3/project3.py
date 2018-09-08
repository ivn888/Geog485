#  Makes a separate shapefile for each type of amenity (schools, hospitals, places of worship) within the boundary of El Salvador.
#  Once the new amenity shapefiles are created, the "source" field is added to them and populated with 'OpenStreetMap'.

import arcpy
arcpy.env.workspace = "C:\\Geog485\\Lesson3\\Project3\\Data"
arcpy.env.overwriteOutput = True

centralAmerica = "CentralAmerica.shp"
osmPoints = "OSMpoints.shp"
amenities = ["school", "hospital", "place_of_worship"]
country = "El Salvador"

# Create a query string for the selected country
countrySelectionClause = '"NAME" = ' + "'" + country + "'"

# Make a feature layer for the selected country (El Salvador)
arcpy.MakeFeatureLayer_management(centralAmerica, "SelectedCountryLayer", countrySelectionClause)

# Create the shapefiles for each amenity
try:
    for amenity in amenities:
        # Create a query string for the selected amenity
        amenitySelectionClause = '"amenity" = ' + "'" + amenity + "'"

        # Select the amenity and make a new layer
        arcpy.MakeFeatureLayer_management(osmPoints, "SelectedAmenityLayer", amenitySelectionClause)

        # Apply a selection to the SelectedAmenityLayer (only select amenities contained by the selected country)
        arcpy.SelectLayerByLocation_management("SelectedAmenityLayer", "CONTAINED_BY", "SelectedCountryLayer")

        # Use CopyFeatures to create a new feature class from the selected data
        arcpy.CopyFeatures_management("SelectedAmenityLayer", amenity + ".shp")

        # Add the "source" field
        arcpy.AddField_management(amenity + ".shp", "source", "TEXT", 100)

        # Create an update cursor for the amenity
        with arcpy.da.UpdateCursor(amenity + ".shp", ("source",)) as cursor:
            for row in cursor:
                row[0] = "OpenStreetMap"
                cursor.updateRow(row)

except:
    print "Creating the shapefiles for each amenity failed."

# Delete the feature layers even if there is an exception (error) raised
finally:
    arcpy.Delete_management("SelectedCountryLayer")
    arcpy.Delete_management("SelectedAmenityLayer")
