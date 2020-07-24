def appendbase():
    addon_folder = bpy.utils.user_resource('SCRIPTS', "addons")
    path = f"{addon_folder}/Planet-Builder/base.blend"
    obj_name = "Planet"
    
    link = False
    
    with bpy.data.libraries.load(path, link=link) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects if name.startswith(obj_name)]
        
    for obj in data_to.objects:
        if obj is not None:
            bpy.context.collection.objects.link(obj)
    return{'FINISHED'}


def gettex(name, file):
    mat = bpy.data.materials['Planet']
    nodes = mat.node_tree.nodes
    node_name = nodes[name]
    img = bpy.data.textures.new(f"{name}", "IMAGE")
    img = bpy.data.images.load(f'{file}{name}.png')
    node_name.image = img
    return{'FINISHED'}


def assigntex():
    dir = bpy.context.scene.file_path
    
    tex_file = f'{dir}output/'
    gettex('pos_x', tex_file)
    gettex('pos_y', tex_file)
    gettex('pos_z', tex_file)
    gettex('neg_x', tex_file)
    gettex('neg_y', tex_file)
    gettex('neg_z', tex_file)
    return{'FINISHED'}
        
def makeround():
    ob = bpy.context.scene.objects["Planet"]
    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.subdivide(number_cuts=6, smoothness=1)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.modifier_add(type='SUBSURF')
    return{'FINISHED'}
        
        
