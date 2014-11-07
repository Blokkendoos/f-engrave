import os
from subprocess import Popen, PIPE

from util import fmessage, VERSION, TTF_AVAILABLE
from . import parse_cxf


def Read_font_file(settings):
    '''
    Read a font file (.cxf, .ttf)
    '''

    filename = settings.get_fontfile()

    if not os.path.isfile(filename):
        return

    fileName, fileExtension = os.path.splitext(filename)
    # self.current_input_file.set( os.path.basename(filename) )

    segarc = settings.get('segarc')

    TYPE = fileExtension.upper()
    if TYPE == '.CXF':
        with open(filename, 'r') as fontfile:
            # build stroke lists from font file
            return parse_cxf(fontfile, segarc)

    elif TYPE == '.TTF':
        option = '-e' if settings.get('ext_char') else ''

        cmd = ["ttf2cxf_stream", option, filename, "STDOUT"]
        try:
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate()
            if VERSION == 3:
                fontfile = bytes.decode(stdout).split("\n")
            else:
                fontfile = stdout.split("\n")

            # build stroke lists from font file
            settings.set('input_type', 'text')
            return parse_cxf(fontfile, segarc)
        except:
            fmessage("Unable To open True Type (TTF) font file: %s" % (filename))
    else:
        pass


def list_fonts(settings):
    try:
        font_files = os.listdir(settings.get('fontdir'))
        font_files.sort()
    except:
        font_files = " "

    font_list = []
    for name in font_files:
        if 'CXF' in name.upper() or ('TTF' in name.upper() and TTF_AVAILABLE):
            font_list.append(name)

    return font_list
