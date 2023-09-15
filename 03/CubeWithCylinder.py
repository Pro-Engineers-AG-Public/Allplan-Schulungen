import NemAll_Python_Geometry as Geometry
import NemAll_Python_BaseElements as BaseElements
import NemAll_Python_BasisElements as BasisElements


class CubeWithCylinder(object):
    X_AXIS = Geometry.Line3D(Geometry.Point3D(), Geometry.Point3D(1, 0, 0))
    Y_AXIS = Geometry.Line3D(Geometry.Point3D(), Geometry.Point3D(0, 1, 0))
    Z_AXIS = Geometry.Line3D(Geometry.Point3D(), Geometry.Point3D(0, 0, 1))

    def __init__(self, build_ele, doc):
        self._build_ele = build_ele
        self._doc = doc

    def create(self):
        width = self._build_ele.Width.value
        length = self._build_ele.Length.value
        height = self._build_ele.Height.value

        placement = Geometry.AxisPlacement3D()
        brep = Geometry.BRep3D.CreateCuboid(placement, length, width, height)

        brep = self.transform(brep)

        com_prop = BaseElements.CommonProperties()
        com_prop.GetGlobalProperties()
        return BasisElements.ModelElement3D(com_prop, brep)

    def transform(self, brep):
        translation_point = self._build_ele.Translation.value

        x_rotation = Geometry.Angle(self._build_ele.RotationX.value)
        y_rotation = Geometry.Angle(self._build_ele.RotationY.value)
        z_rotation = Geometry.Angle(self._build_ele.RotationZ.value)

        matrix = Geometry.Matrix3D()

        result = matrix.Rotation(CubeWithCylinder.X_AXIS, x_rotation)
        if not result:
            raise Exception("Rotation around x axis failed")

        result = matrix.Rotation(CubeWithCylinder.Y_AXIS, y_rotation)
        if not result:
            raise Exception("Rotation around y axis failed")

        result = matrix.Rotation(CubeWithCylinder.Z_AXIS, z_rotation)
        if not result:
            raise Exception("Rotation around z axis failed")

        matrix.Translate(Geometry.Vector3D(translation_point))

        return Geometry.Transform(brep, matrix)
