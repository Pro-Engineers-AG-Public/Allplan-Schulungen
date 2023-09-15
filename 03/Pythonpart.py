import NemAll_Python_Geometry as Geometry
import NemAll_Python_BaseElements as BaseElements
import NemAll_Python_BasisElements as BasisElements

VALID_ALLPLAN_VERSIONS = [2023, 2024]


def check_allplan_version(build_ele, version):
    """
    Check the current Allplan version

    Args:
        build_ele: the building element.
        version:   the current Allplan version

    Returns:
        True/False if version is supported by this script
    """

    # Delete unused arguments
    del build_ele

    for item in VALID_ALLPLAN_VERSIONS:
        if str(item) in version:
            return True

    # Disable not valid versions
    return False


def create_element(build_ele, doc):
    """
    Creation of element

    Args:
        build_ele: the building element.
        doc:       input document
    """
    model_ele_list = []
    handle_list = []

    cableCart = CableCart(build_ele, doc)
    model_ele_list.append(cableCart.create())

    return (model_ele_list, handle_list)


class CableCart(object):
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
        com_prop = BaseElements.CommonProperties()
        com_prop.GetGlobalProperties()

        brep = Geometry.BRep3D.CreateCuboid(placement, length, width, height)

        brep = self.transform(brep)

        return BasisElements.ModelElement3D(com_prop, brep)

    def transform(self, brep):
        translation_point = self._build_ele.Translation.value

        x_rotation = Geometry.Angle(self._build_ele.RotationX.value)
        y_rotation = Geometry.Angle(self._build_ele.RotationY.value)
        z_rotation = Geometry.Angle(self._build_ele.RotationZ.value)

        matrix = Geometry.Matrix3D()

        result = matrix.Rotation(CableCart.X_AXIS, x_rotation)
        if not result:
            raise Exception("Rotation around x axis failed")

        result = matrix.Rotation(CableCart.Y_AXIS, y_rotation)
        if not result:
            raise Exception("Rotation around y axis failed")

        result = matrix.Rotation(CableCart.Z_AXIS, z_rotation)
        if not result:
            raise Exception("Rotation around z axis failed")

        matrix.Translate(Geometry.Vector3D(translation_point))

        return Geometry.Transform(brep, matrix)
