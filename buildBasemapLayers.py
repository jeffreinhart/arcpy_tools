#-------------------------------------------------------------------------------
# Name:        buildBasemapLayers.py
# Purpose:     Build group layers with zooms for web based basemap. Need a blank
#              group layer saved as lyr to be able to add a group layer.
#
# Author:      Jeff Reinhart
#
# Created:     11/01/2015
#-------------------------------------------------------------------------------

import arcpy

inDoc = r'<your_map_document>.mxd'
tempGroupLayer = r'<your_temp_layer>.lyr'
mxd = arcpy.mapping.MapDocument(inDoc)
dataFrame = arcpy.mapping.ListDataFrames(mxd)[0]

scaleList = [4622324, 2311162, 1155581, 577791, 288895, 144448, 72224, 36112, 18056, 9028, 4514, 2257, 1128]

for scale in scaleList:
    # create layer object
    groupLayer = arcpy.mapping.Layer(tempGroupLayer)
    # rename the layer
    layerName = "1:"+str(scale)
    groupLayer.name = layerName
    # change the min and max scale
    groupLayer.minScale = scale+1
    groupLayer.maxScale = scale-1
    # add the layer and save
    tempLayer = arcpy.mapping.AddLayer(dataFrame, groupLayer, "TOP")

# save the mxd
mxd.save()