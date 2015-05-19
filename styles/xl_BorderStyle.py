#Copyright(c) 2015, David Mans, Konrad Sobon
# @arch_laboratory, http://archi-lab.net, http://neoarchaic.net

import clr
import sys

pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

import os
import os.path
appDataPath = os.getenv('APPDATA')
bbPath = appDataPath + r"\Dynamo\0.8\packages\Bumblebee\extra"
if bbPath not in sys.path:
	sys.path.Add(bbPath)

import bumblebee as bb

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

lineType = IN[0]
weight = IN[1]
color = IN[2]

borderStyle = bb.BBBorderStyle()

if lineType != None:
	borderStyle.lineType = lineType
if weight != None:
	borderStyle.weight = weight
if color != None:
	borderStyle.color = color

#Assign your output to the OUT variable
OUT = borderStyle