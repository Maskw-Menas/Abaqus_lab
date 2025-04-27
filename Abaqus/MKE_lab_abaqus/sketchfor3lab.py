# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-5 replay file
# Internal Version: 2015_08_18-18.37.49 135153
# Run by Evgeny on Mon Mar 10 12:13:41 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=176.62890625, 
    height=118.336799621582)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(pathName='D:/University/8-semak/MKE/3laba.cae')
#: The model database "D:\University\8-semak\MKE\3laba.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2817.83, 
    farPlane=2839.03, width=63.3679, height=30.7501, viewOffsetX=-0.781127, 
    viewOffsetY=1.43377)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='D:/SystemSoft/abacus/Job-1.odb')
#: Model: D:/SystemSoft/abacus/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3292.79, 
    farPlane=4707.21, width=0.623976, height=0.302792, viewOffsetX=-2.09685, 
    viewOffsetY=3.62699)
session.Path(name='Path-1', type=NODE_LIST, expression=(('PART-1-1', (11, 
    '190:177:-1', 10, '250:236:-1', 16, '429:415:-1', 13, '218:205:-1', 12, )), 
    ))
session.Path(name='Path-2', type=NODE_LIST, expression=(('PART-1-1', (371, 
    '1226:1239:1', 344, '1443:1541:7', 430, '1892:1990:7', 399, '1324:1337:1', 372, )),
    ))
session.Path(name='Path-3', type=NODE_LIST, expression=(('PART-1-1', (370, 
    '1240:1253:1', 345, '1442:1540:7', 431, '1891:1989:7', 398, '1338:1351:1', 373, )),
    ))
session.Path(name='Path-4', type=NODE_LIST, expression=(('PART-1-1', (369, 
    '1254:1267:1', 346, '1441:1539:7', 432, '1890:1988:7', 397, '1352:1365:1', 374, )),
    ))
session.Path(name='Path-5', type=NODE_LIST, expression=(('PART-1-1', (368, 
    '1268:1281:1', 347, '1440:1538:7', 433, '1889:1987:7', 396, '1366:1379:1', 375, )),
    ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))
pth = session.paths['Path-1']
session.XYDataFromPath(name='path1_x_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-2']
session.XYDataFromPath(name='path2_x_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-3']
session.XYDataFromPath(name='path3_x_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-4']
session.XYDataFromPath(name='path4_x_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-5']
session.XYDataFromPath(name='path5_x_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))
pth = session.paths['Path-1']
session.XYDataFromPath(name='path1_x_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-2']
session.XYDataFromPath(name='path2_x_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-3']
session.XYDataFromPath(name='path3_x_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-4']
session.XYDataFromPath(name='path4_x_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-5']
session.XYDataFromPath(name='path5_x_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'))
pth = session.paths['Path-1']
session.XYDataFromPath(name='path1_x_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-2']
session.XYDataFromPath(name='path2_x_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-3']
session.XYDataFromPath(name='path3_x_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-4']
session.XYDataFromPath(name='path4_x_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-5']
session.XYDataFromPath(name='path5_x_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E11'))
session.XYDataFromPath(name='path1_x_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-2']
session.XYDataFromPath(name='path2_x_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-3']
session.XYDataFromPath(name='path3_x_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-4']
session.XYDataFromPath(name='path4_x_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-5']
session.XYDataFromPath(name='path5_x_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E22'))
pth = session.paths['Path-1']
session.XYDataFromPath(name='path1_x_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-2']
session.XYDataFromPath(name='path2_x_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-3']
session.XYDataFromPath(name='path3_x_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-4']
session.XYDataFromPath(name='path4_x_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-5']
session.XYDataFromPath(name='path5_x_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E12'))
pth = session.paths['Path-1']
session.XYDataFromPath(name='path1_x_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-2']
session.XYDataFromPath(name='path2_x_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-3']
session.XYDataFromPath(name='path3_x_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-4']
session.XYDataFromPath(name='path4_x_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
pth = session.paths['Path-5']
session.XYDataFromPath(name='path5_x_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
#вывод графиков
x0 = session.xyDataObjects['path1_x_s11']
session.writeXYReport(fileName='path1_x_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path1_x_s12']
session.writeXYReport(fileName='path1_x_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path1_x_s22']
session.writeXYReport(fileName='path1_x_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path1_x_e11']
session.writeXYReport(fileName='path1_x_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path1_x_e12']
session.writeXYReport(fileName='path1_x_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path1_x_e22']
session.writeXYReport(fileName='path1_x_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path2_x_s11']
session.writeXYReport(fileName='path2_x_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path2_x_s12']
session.writeXYReport(fileName='path2_x_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path2_x_s22']
session.writeXYReport(fileName='path2_x_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path2_x_e11']
session.writeXYReport(fileName='path2_x_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path2_x_e12']
session.writeXYReport(fileName='path2_x_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path2_x_e22']
session.writeXYReport(fileName='path2_x_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path3_x_s11']
session.writeXYReport(fileName='path3_x_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path3_x_s12']
session.writeXYReport(fileName='path3_x_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path3_x_s22']
session.writeXYReport(fileName='path3_x_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path3_x_e11']
session.writeXYReport(fileName='path3_x_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path3_x_e12']
session.writeXYReport(fileName='path3_x_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path3_x_e22']
session.writeXYReport(fileName='path3_x_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path4_x_s11']
session.writeXYReport(fileName='path4_x_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path4_x_s12']
session.writeXYReport(fileName='path4_x_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path4_x_s22']
session.writeXYReport(fileName='path4_x_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path4_x_e11']
session.writeXYReport(fileName='path4_x_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path4_x_e12']
session.writeXYReport(fileName='path4_x_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path4_x_e22']
session.writeXYReport(fileName='path4_x_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path5_x_s11']
session.writeXYReport(fileName='path5_x_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path5_x_s12']
session.writeXYReport(fileName='path5_x_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path5_x_s22']
session.writeXYReport(fileName='path5_x_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path5_x_e11']
session.writeXYReport(fileName='path5_x_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path5_x_e12']
session.writeXYReport(fileName='path5_x_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path5_x_e22']
session.writeXYReport(fileName='path5_x_e22.rpt', xyData=(x5))

#создание графики тайм фреймов
session.Path(name='Path-6', type=NODE_LIST, expression=(('PART-1-1', (15, 235, 
    16, '430:436:1', 26, '589:592:1', 36, )), ))
   
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_1_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_1_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_1_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_1_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_1_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_1_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
    
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_10_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_10_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_10_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_10_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_10_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_10_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
    
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=15)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_15_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_15_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_15_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_15_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_15_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_15_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)


session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=20)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_20_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_20_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_20_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_20_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_20_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_20_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
    

session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=30)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_30_s11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_30_s12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_30_s22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E11'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_30_e11', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E12'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_30_e12', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'E22'))
pth = session.paths['Path-6']
session.XYDataFromPath(name='path6_30_e22', path=pth, 
    includeIntersections=False, projectOntoMesh=False, pathStyle=PATH_POINTS, 
    numIntervals=10, projectionTolerance=0, shape=UNDEFORMED, 
    labelType=TRUE_DISTANCE)

#вывод графиков тайм фреймов
x0 = session.xyDataObjects['path6_1_s11']
session.writeXYReport(fileName='path6_1_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path6_1_s12']
session.writeXYReport(fileName='path6_1_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path6_1_s22']
session.writeXYReport(fileName='path6_1_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path6_1_e11']
session.writeXYReport(fileName='path6_1_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path6_1_e12']
session.writeXYReport(fileName='path6_1_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path6_1_e22']
session.writeXYReport(fileName='path6_1_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path6_10_s11']
session.writeXYReport(fileName='path6_10_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path6_10_s12']
session.writeXYReport(fileName='path6_10_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path6_10_s22']
session.writeXYReport(fileName='path6_10_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path6_10_e11']
session.writeXYReport(fileName='path6_10_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path6_10_e12']
session.writeXYReport(fileName='path6_10_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path6_10_e22']
session.writeXYReport(fileName='path6_10_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path6_15_s11']
session.writeXYReport(fileName='path6_15_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path6_15_s12']
session.writeXYReport(fileName='path6_15_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path6_15_s22']
session.writeXYReport(fileName='path6_15_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path6_15_e11']
session.writeXYReport(fileName='path6_15_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path6_15_e12']
session.writeXYReport(fileName='path6_15_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path6_15_e22']
session.writeXYReport(fileName='path6_15_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path6_20_s11']
session.writeXYReport(fileName='path6_20_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path6_20_s12']
session.writeXYReport(fileName='path6_20_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path6_20_s22']
session.writeXYReport(fileName='path6_20_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path6_20_e11']
session.writeXYReport(fileName='path6_20_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path6_20_e12']
session.writeXYReport(fileName='path6_20_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path6_20_e22']
session.writeXYReport(fileName='path6_20_e22.rpt', xyData=(x5))

x0 = session.xyDataObjects['path6_30_s11']
session.writeXYReport(fileName='path6_30_s11.rpt', xyData=(x0))
x1 = session.xyDataObjects['path6_30_s12']
session.writeXYReport(fileName='path6_30_s12.rpt', xyData=(x1))
x2 = session.xyDataObjects['path6_30_s22']
session.writeXYReport(fileName='path6_30_s22.rpt', xyData=(x2))
x3 = session.xyDataObjects['path6_30_e11']
session.writeXYReport(fileName='path6_30_e11.rpt', xyData=(x3))
x4 = session.xyDataObjects['path6_30_e12']
session.writeXYReport(fileName='path6_30_e12.rpt', xyData=(x4))
x5 = session.xyDataObjects['path6_30_e22']
session.writeXYReport(fileName='path6_30_e22.rpt', xyData=(x5))
