def unregister():
    bpy.utils.unregister_class(MakeTextures)
    bpy.utils.unregister_class(MakePlanet)
    bpy.utils.unregister_class(_PT_PlanetbuilderPanel)
    bpy.utils.unregister_class(Clearall)
    bpy.utils.unregister_class(TextureRes)
    del bpy.types.WindowManager.texture_res
    del bpy.types.Scene.file_path

if __name__ == '__main__':
    register()