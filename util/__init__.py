import sys
import datetime

import externals
from icon import *

IN_AXIS = "AXIS_PROGRESS_BAR" in os.environ

# Setting QUIET to True will stop almost all console messages
QUIET = False

VERSION = sys.version_info[0]

# entry value check return codes:
OK = 0  # value is ok (may require recalculation)
NOR = 1  # value is a valid number change that does not require recalc
INV = 2  # value is invalid
NAN = 3  # value is not a number

if VERSION == 3:
    # from tkinter import *
    # from tkinter.filedialog import *
    import tkinter.messagebox
    MAXINT = sys.maxsize
else:
    # from Tkinter import *
    # from tkFileDialog import *
    import tkMessageBox
    MAXINT = sys.maxint


def fmessage(text, newline=True):
    if IN_AXIS or QUIET:
        return
    try:
        sys.stdout.write(text)
        if newline:
            sys.stdout.write("\n")
    except:
        pass


PIL = False
OVD_AVAILABLE = False
TTF_AVAILABLE = False
POTRACE_AVAILABLE = False

try:
    PIL = externals.check_pil()
    OVD_AVAILABLE = externals.check_ovd()
    TTF_AVAILABLE = externals.check_ttf()
    POTRACE_AVAILABLE = externals.check_potrace()
except Exception, e:
    fmessage(e)


def f_engrave_version():
    return '1.65b'


def header_text():
    header = []
    # todays_date = datetime.date.today().strftime("%B %d, %Y")
    todays_datetime = datetime.datetime.now().strftime("%I:%M %p %B %d, %Y")
    header.append('(Code generated by OOF-Engrave-' + f_engrave_version() + '.py widget )')
    header.append('(by JvO 2018 (refactored F-Engrave by Scorch - 2017 )')
    header.append('(file created ' + todays_datetime + ')')
    header.append('(=========================================================)')

    return header


def message_box(title, message):
    if VERSION == 3:
        tkinter.messagebox.showinfo(title, message)
    else:
        tkMessageBox.showinfo(title, message)
        pass


def message_ask_ok_cancel(title, message):
    if VERSION == 3:
        result = tkinter.messagebox.askokcancel(title, message)
    else:
        result = tkMessageBox.askokcancel(title, message)
    return result


def position_window(win, width, height):
    """
    centers a tkinter Toplevel window to its master
    Source: https://stackoverflow.com/questions/36050192/how-to-position-toplevel-widget-relative-to-root-window
    :param width: the Toplevel window width
    :param height: the Toplevel window height
    :param win: the Toplevel window to center
    """
    win.update_idletasks()

    master = win.master
    x = master.winfo_x()
    y = master.winfo_y()

    x -= width
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()
