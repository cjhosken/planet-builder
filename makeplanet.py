class MakePlanet(Operator):
    bl_label = 'Make Planet'
    bl_idname = 'mk.planet'
    bl_description = 'Builds a planet from tiles.'
    bl_options = {'REGISTER','UNDO'}
    
    
    def execute(self, context):
        #if bpy.context.scene.file_path == "" or RuntimeError:
        #    ShowMessageBox("No File Path Found.", "ERROR", 'ERROR')
        #    return{'CANCELLED'}
        #else:
        #    clear()
        #    appendbase()
        #    assigntex()
        #    makeround()
        #    return{'FINISHED'}
        clear()
        appendbase()
        assigntex()
        makeround()
        return{'FINISHED'}
