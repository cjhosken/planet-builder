def register():
    bpy.utils.register_class(MakeTextures)
    bpy.utils.register_class(MakePlanet)
    bpy.utils.register_class(_PT_PlanetbuilderPanel)
    bpy.utils.register_class(Clearall)
    bpy.utils.register_class(TextureRes)
    bpy.types.WindowManager.texture_res = PointerProperty(type=TextureRes)
    bpy.types.Scene.file_path = StringProperty \
        (
        name = '',
        description = 'Select Folder',
        default = '',
        subtype = 'FILE_PATH'
        )