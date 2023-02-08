# Raster_Extents_To_Polygons
Creates a feature class of polygons that show the raster extents for all of the rasters in a directory.  The resulting feature class includes the raster extent, the file name, and the file path.
A toolbox tool is included for easy use in ArcGIS10x and an updated toolbox and script are available for ArcGIS Pro v3.

The generally accepted method to generate raster extent polygons is to push your data to a raster mosaic and use raster mosaic tools to generate the polygons.  This tool does not require a mosaic dataset.  The tool only requires an input directory of rasters and an output feature class.  The directory of rasters should all share the same spatial reference system or some polygons will be created in the incorrect location.  The resulting polygons include two attributes, the full path to the raster, and the raster name.  
I like to run my scripts in a Python IDE (Wing Pro) so opening the script in the IDE and hardcoding the arguments is an option.  The script works with a standard ArcGIS Pro Python interpreter so no cloning is required.  The tool works with a basic ArcGIS license level and does not require a spatial analyst or 3d analyst license.



