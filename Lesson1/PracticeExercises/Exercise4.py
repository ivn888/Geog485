import arcpy

featureClass = "C:/Geog485/Lesson1/suitable_land.shp"

desc = arcpy.Describe(featureClass)
shape = desc.shapeType

print shape
