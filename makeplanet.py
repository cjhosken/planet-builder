import bpy, __init__, plfunctions, texfunctions
from bpy.types import Operator

class MakePlanet(Operator):
    bl_label = 'Make Planet'
    bl_idname = 'mk.planet'
    bl_description = 'Builds a planet from tiles.'
    bl_options = {'REGISTER','UNDO'}
    
    
    def execute(self, context):
        if bpy.context.scene.file_path == "" or RuntimeError:
            __init__.ShowMessageBox("No File Path Found.", "Whoops!", 'ERROR')
            return{'CANCELLED'}
        else:
            texfunctions.clear()
            plfunctions.appendbase()
            plfunctions.assigntex()
            plfunctions.makeround()
            return{'FINISHED'}
