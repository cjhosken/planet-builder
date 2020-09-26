import bpy, os, __init__, texfunctions
from bpy.types import Operator

class MakeTextures(Operator):
    bl_label = 'Make Textures'
    bl_idname = 'mk.textures'
    bl_description = 'Makes large texture tiles (MAY TAKE A LONG TIME)'
    bl_options = {'REGISTER','UNDO'}
    
    def execute(self, context):
        if bpy.context.scene.file_path == "" or RuntimeError:
            __init__.ShowMessageBox("No File Path Found.", "Whoops!", 'ERROR')
            return{'CANCELLED'}
        else:
            dir = context.scene.file_path
            res = context.window_manager.texture_res.resolution
            
            folders = []
            
            for r, d, f in os.walk(dir):
                for dir_name in d:
                    print(dir_name)
                    if dir_name != 'output':
                        files = []
                        for r, d, f in os.walk(f'{dir}{dir_name}/'):
                            texfunctions.clear()
                            for file_name in f:
                                texfunctions.center_cursor()
                                texfunctions.buildgrid(dir_name, file_name)
                                
                            texfunctions.addcam(dir, dir_name)
                            texfunctions.render(dir_name)
            texfunctions.clear()
            return{'FINISHED'}