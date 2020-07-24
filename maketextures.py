class MakeTextures(Operator):
    bl_label = 'Make Textures'
    bl_idname = 'mk.textures'
    bl_description = 'Makes large texture tiles (MAY TAKE A LONG TIME)'
    bl_options = {'REGISTER','UNDO'}
    
    def execute(self, context):
        if bpy.context.scene.file_path == "" or RuntimeError:
            ShowMessageBox("No File Path Found.", "ERROR", 'ERROR')
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
                            clear()
                            for file_name in f:
                                center_cursor()
                                buildgrid(dir_name, file_name)
                                
                            addcam(dir, dir_name)
                            render(dir_name)
            clear()
            return{'FINISHED'}