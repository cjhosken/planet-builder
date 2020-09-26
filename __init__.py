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
    "blender" : (2, 90, 1),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "Planet Builder only works with Solar System HD and Solar System Ultra textures.",
    "category" : "General"
}

from importlib import reload
import bpy, os, sys
from bpy.props import PointerProperty, StringProperty

addon_folder = bpy.utils.user_resource('SCRIPTS', "addons")

try:
    addons_directory = os.path.dirname(__file__)
except:
    pass
try:
    addons_directory = os.path.dirname(bpy.context.space_data.text.filepath)
except:
    pass

print(addons_directory)

sys.path.append(addons_directory)

sys.path.append(addons_directory)
if 'pl-functions' in sys.modules:
    reload(sys.modules['plfunctions'])
if 'makeplanet' in sys.modules:
    reload(sys.modules['makeplanet'])
if 'tex-functions' in sys.modules:
    reload(sys.modules['texfunctions'])
if 'maketextures' in sys.modules:
    reload(sys.modules['maketextures'])
if 'panel' in sys.modules:
    reload(sys.modules['panel'])
import plfunctions
import makeplanet
import texfunctions
import maketextures
import panel

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

def register():
    bpy.utils.register_class(maketextures.MakeTextures)
    bpy.utils.register_class(makeplanet.MakePlanet)
    bpy.utils.register_class(panel._PT_PlanetbuilderPanel)
    bpy.utils.register_class(panel.Clearall)
    bpy.utils.register_class(panel.TextureRes)
    bpy.types.WindowManager.texture_res = PointerProperty(type=panel.TextureRes)
    bpy.types.Scene.file_path = StringProperty \
        (
        name = '',
        description = 'Select Folder',
        default = '',
        subtype = 'FILE_PATH'
        )

def unregister():
    bpy.utils.unregister_class(maketextures.MakeTextures)
    bpy.utils.unregister_class(makeplanet.MakePlanet)
    bpy.utils.unregister_class(panel._PT_PlanetbuilderPanel)
    bpy.utils.unregister_class(panel.Clearall)
    bpy.utils.unregister_class(panel.TextureRes)
    del bpy.types.WindowManager.texture_res
    del bpy.types.Scene.file_path

if __name__ == '__main__':
    try:
        unregister()
    except:
        pass
    register()