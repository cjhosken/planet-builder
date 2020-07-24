def center_cursor():
    bpy.context.scene.cursor.location[0] = 0
    bpy.context.scene.cursor.location[1] = 0
    bpy.context.scene.cursor.location[2] = 0
    bpy.context.scene.cursor.rotation_euler[0] = 0
    bpy.context.scene.cursor.rotation_euler[1] = 0
    bpy.context.scene.cursor.rotation_euler[2] = 0
    return{'FINISHED'}

def buildgrid(dir_name, file_name):
    dir = bpy.context.scene.file_path
    res = bpy.context.window_manager.texture_res.resolution
    path = (f'{dir}{dir_name}/')
    start = getlargest(path)
        
    if file_name.startswith(start[0]):
        x = int((file_name.split('_')[2])[:-4])
        y = int(file_name.split('_')[1])
        bpy.context.scene.cursor.location[0] = x
        bpy.context.scene.cursor.location[1] = -y
        bpy.ops.import_image.to_plane(files=[{"name": file_name}], directory=path, offset_amount=0,height=1, shader='SHADELESS')
        bpy.ops.object.rotation_clear(clear_delta=False)
    return{'FINISHED'}


def getlargest(path):
    for r, d, f in os.walk(path):
            list_of_files = []
            for name in f:
                if name.endswith(('_0_0.png')):
                    list_of_files.append(name)
            largest = max(list_of_files)
    return largest


def buildfolder(dir):
    new_dir = f'{dir}output'    
    
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    
    return{'FINISHED'}


def render(dir_name):
    dir = bpy.context.scene.file_path
    
    new_dir = f'{dir}output'
    
    buildfolder(dir)
    
    bpy.context.scene.render.filepath = f'{new_dir}/{dir_name}.png'
    
    my_areas = bpy.context.workspace.screens[0].areas
    
    for area in my_areas:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.overlay.show_overlays = False
                    space.shading.type = 'SOLID'
                    space.shading.color_type = 'TEXTURE'
                    space.shading.light = 'FLAT'
                    bpy.context.scene.view_settings.view_transform = 'Standard'
                    bpy.context.scene.render.image_settings.color_mode = 'RGB'
                    bpy.context.scene.render.image_settings.color_depth = '16'
                    space.shading.show_object_outline = False
                    bpy.context.scene.camera = bpy.data.objects["Camera"]
                    bpy.ops.render.opengl(write_still = True, view_context = True)
    return{'FINISHED'}


def clear():
    for image in bpy.data.images:
        bpy.data.images.remove(image)
    for mesh in bpy.data.meshes:
        bpy.data.meshes.remove(mesh)
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)
    for mat in bpy.data.materials:
        bpy.data.materials.remove(mat)
    for cam in bpy.data.cameras:
        bpy.data.cameras.remove(cam)
    return{'FINISHED'}


def entercam():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'


def addcam(dir, dir_name):
    file = f'{dir}{dir_name}/'
    res = bpy.context.window_manager.texture_res.resolution
    length = []
    length = math.sqrt(len(os.listdir(file)))
    
    if res == '4k':
        length = 4
    elif res == '8k':
        length = 8
    elif res == '16k':
        length = 16
    elif res == '32k':
        length = 32
    elif res == '64k':
        length = 64
    elif res == '128k':
        length = 128
    
    x = (length/2) - 0.5
    y = (length/2) - 0.5
    z = 5
    
    bpy.context.scene.cursor.location[0] = x
    bpy.context.scene.cursor.location[1] = -y
    bpy.context.scene.cursor.location[2] = z
    bpy.ops.object.camera_add()
    bpy.context.object.data.type = 'ORTHO'
    bpy.context.object.data.ortho_scale = length
    bpy.context.scene.render.resolution_x = length*258
    bpy.context.scene.render.resolution_y = length*258
    entercam()
    center_cursor()
        
    
    return{'FINISHED'}