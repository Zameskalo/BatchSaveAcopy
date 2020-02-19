import arcpy, sys, os, string 

arcpy.env.overwriteOutput = True

mxdList = string.split(arcpy.GetParameterAsText(0), ";") 
outloc = arcpy.GetParameterAsText(1) 
version = arcpy.GetParameterAsText(2) 

suffix = "_"+ version.replace(".", "") 

for item in mxdList: 
    item = item.strip('\'') 
    mxd = arcpy.mapping.MapDocument(item) 
    base = os.path.basename(item) 
    base = os.path.splitext(base)[0] + os.path.splitext(base)[1]
    mxd.saveACopy(outloc + os.sep + "10_"  + base, version) 
    arcpy.AddMessage(os.path.basename(item) + " has been converted") 