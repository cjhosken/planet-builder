import bpy, __init__, makeplanet, maketextures, texfunctions
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import EnumProperty


class _PT_PlanetbuilderPanel(Panel):
    bl_label = "Planet Builder"
    bl_idname = "PANEL_PT_planetbuilder"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        
        row.prop(context.scene, 'file_path')
        row = layout.row()
        
        row.prop(context.window_manager.texture_res, 'resolution', expand=True)
        row = layout.row()
        row.operator('mk.textures', text='Make Textures', icon="VIEW_ORTHO" )
        row = layout.row()
        row.operator('mk.planet', text="Make Planet", icon='WORLD')
        row.operator('cl.all', text="", icon='X')
        

class TextureRes(PropertyGroup):
    resolution: EnumProperty(
        items=[
            ('4k', '4k', '', '', 0),
            ('8k', '8k', '', '', 1),
            ('16k', '16k', '', '', 2),
            ('32k', '32k', '', '', 3),
            ('64k', '64k', '', '', 4),
            ('128k', '128k', '', '', 5),
        ],
        default='4k'
    )
    
    
class Clearall(Operator):
    bl_label = "Clear All"
    bl_idname = 'cl.all'
    bl_description = "Delete all objects, textures, and materials"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        texfunctions.clear()
        return{'FINISHED'}
