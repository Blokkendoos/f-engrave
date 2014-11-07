from geometry import Character, Line, Font
from geometry.boundingbox import BoundingBox

from dxf_class import DXF_CLASS


def parse(dxf_file, segarc, new_origin=True):
    # Initialize / reset
    font = Font()
    key = None

    DXF_source = " "
    dxf_import = DXF_CLASS()
    dxf_import.GET_DXF_DATA(dxf_file, tol_deg=segarc)
    dxfcoords = dxf_import.DXF_COORDS_GET(new_origin)

    if "POTRACE" in dxf_import.comment.upper():
        DXF_source = "POTRACE"
    if "INKSCAPE" in dxf_import.comment.upper():
        DXF_source = "INKSCAPE"

    # save the character to our dictionary
    key = ord("F")
    stroke_list = []
    bbox = BoundingBox()

    for line in dxfcoords:
        line = Line(line[0:4])

        stroke_list.append(line)
        bbox.extend(line)

    font.add_character(Character(key, stroke_list))

    return font, DXF_source
