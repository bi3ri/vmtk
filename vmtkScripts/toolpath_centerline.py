import vtk

#from vmtk.vmtkcenterlines import vmtkCenterlines
from vmtkcenterlines import vmtkCenterlines


def loadStl(fname):
    """Load the given STL file, and return a vtkPolyData object."""
    reader = vtk.vtkSTLReader()
    reader.SetFileName(fname)
    reader.Update()
    return reader.GetOutput()

class ToolpathCenterline:

    print("egal")




#xyz der punkte festlegen und dann durch alle punkte gehen und die naehsten punkte waehlen
#versuch vmtkPointListSeedSelector!!!!
#       minZId = -1
        # maxZId = -1
        # minZ = 1E8
        # maxZ = -1E8

        # for id in range(self._SeedIds.GetNumberOfIds()):
        #     currentZ = self._Surface.GetPoint(self._SeedIds.GetId(id))[2]
        #     if (currentZ < minZ):
        #         minZ = currentZ
        #         minZId = id

        #     if (currentZ > maxZ):
        #         maxZ = currentZ
        #         maxZId = id

if __name__=='__main__':
    centerline = vmtkCenterlines()

    surface = vtk.vtkPolyData()
    surface = loadStl('/home/bi3ri/tube_ws/src/tubular_toolpath_creator/data/coil_out.stl')

    centerline.Surface = surface
    centerline.SeedSelector = True
    centerline.SeedSelectorName = 'openprofiles'
    centerline.Execute()
