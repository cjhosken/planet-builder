# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Planet Builder",
    "author" : "Christopher Hosken",
    "description" : "",
    "blender" : (2, 80, 3),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "Planet Builder only works with Solar System HD and Solar System Ultra textures.",
    "category" : "General"
}

import bpy, os, math, pathlib, shutil
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import StringProperty, BoolProperty, PointerProperty, EnumProperty

homedir = os.path.expanduser("~/")

addon_folder = bpy.utils.user_resource('SCRIPTS', "addons")

#addon_folder = '/home/cjhosken/Documents/Visual Studio Code/Blender_Addons'

with open(f"{addon_folder}/Planet-Builder/tex-functions.py") as txfun:
    txfun_file = txfun.read()

with open(f"{addon_folder}/Planet-Builder/maketextures.py") as texmk:
    texmk_file = texmk.read()

with open(f"{addon_folder}/Planet-Builder/pl-functions.py") as plfun:
    plfun_file = plfun.read()

with open(f"{addon_folder}/Planet-Builder/makeplanet.py") as plmk:
    plmk_file = plmk.read()

with open(f"{addon_folder}/Planet-Builder/panel.py") as panel:
    panel_file = panel.read()

with open(f"{addon_folder}/Planet-Builder/register.py") as reg:
    reg_file = reg.read()

with open(f"{addon_folder}/Planet-Builder/unregister.py") as unreg:
    unreg_file = unreg.read()

exec(txfun_file + "\n" + texmk_file + "\n" + plfun_file + "\n" + plmk_file + "\n" + panel_file + "\n" + reg_file + "\n" + unreg_file)

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)



# Addon Path: bpy.utils.user_resource('SCRIPTS, "addons")

# Testing Path: /home/cjhosken/Documents/Visual\Studio\Code/Blender_Addons
