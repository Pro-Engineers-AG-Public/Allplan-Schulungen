from .CubeWithCylinder import CubeWithCylinder


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

    cableCart = CubeWithCylinder(build_ele, doc)
    model_ele_list.append(cableCart.create())

    return (model_ele_list, handle_list)
