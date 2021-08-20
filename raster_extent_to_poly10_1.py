try:
    import sys, traceback, os
    import arcpy
    arcpy.AddMessage("Another Lummi GIS geoprocessing tool by Gerry Gabrisch, GISP - 1/25/2016  geraldg@lummi-nsn.gov...")
    arcpy.AddMessage("Version 2.0  ...\n")
    
    inDir = arcpy.GetParameterAsText(0)
    outFile = arcpy.GetParameterAsText(1)
    
    feature_classes = []
    walk = arcpy.da.Walk(inDir, datatype="RasterDataset", type="All")
    
    for dirpath, dirnames, filenames in walk:
        for filename in filenames:
            feature_classes.append(os.path.join(dirpath, filename))

    arcpy.CreateFeatureclass_management(os.path.dirname(outFile),os.path.basename(outFile),"POLYGON")
    
    arcpy.AddField_management(outFile,"RasterName", "String","","",100)
    arcpy.AddField_management(outFile,"RasterPath", "String","","",250)
    
    cursor = arcpy.InsertCursor(outFile)
    point = arcpy.Point()
    array = arcpy.Array()
    corners = ["lowerLeft", "lowerRight", "upperRight", "upperLeft"]
   
    for Ras in feature_classes:
        feat = cursor.newRow()  
        r = arcpy.Raster(Ras)
        for corner in corners:    
            point.X = getattr(r.extent, "%s" % corner).X
            point.Y = getattr(r.extent, "%s" % corner).Y
            array.add(point)
        array.add(array.getObject(0))
        polygon = arcpy.Polygon(array)
        feat.shape = polygon
        feat.setValue("RasterName", Ras.split('\\')[-1])
        feat.setValue("RasterPath", Ras)
        cursor.insertRow(feat)
        array.removeAll()
    del feat
    del cursor  
    
    
    arcpy.AddMessage("All Done :)")
except arcpy.ExecuteError: 
    msgs = arcpy.GetMessages(2) 
    arcpy.AddError(msgs) 
    print msgs
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)
    print pymsg + "\n"
    print msgs

