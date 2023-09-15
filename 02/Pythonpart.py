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

    print(version)

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

    del doc

    model_ele_list = []
    handle_list = []

    placement = Geometry.AxisPlacement3D()

    com_prop = BaseElements.CommonProperties()
    com_prop.GetGlobalProperties()

    width = build_ele.Width.value
    length = build_ele.Length.value
    height = build_ele.Height.value

    brep = Geometry.BRep3D.CreateCuboid(placement, length, width, height)
    model_ele_list.append(BasisElements.ModelElement3D(com_prop, brep))

    return (model_ele_list, handle_list)
