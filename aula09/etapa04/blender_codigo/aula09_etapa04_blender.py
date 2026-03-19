import bpy

# 1. Limpa a cena inicial
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 2. Cria as formas (Esfera, Cubo, Cone)
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0,0,0))
bpy.ops.mesh.primitive_cube_add(location=(3,0,0))
bpy.ops.mesh.primitive_cone_add(location=(-3,0,0))

# 3. Configura a iluminação (Luz do Sol)
bpy.ops.object.light_add(type='SUN', location=(5,5,10))
bpy.context.active_object.data.energy = 5

# 4. Configura a Câmera
bpy.ops.object.camera_add(location=(8,-8,5))
cam = bpy.context.active_object
cam.rotation_euler = (1.1, 0, 0.785)
bpy.context.scene.camera = cam

# 5. Configurações de Renderização (Salvando na pasta da Aula 09)
caminho_pasta = 'C:/Users/Michael Maciel/OneDrive/Documentos/Michael/UNIFG/Computacao_grafica_e_realidade_virtual/exec_opencv/aula09/'
bpy.context.scene.render.filepath = caminho_pasta + 'blender_render####'
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.resolution_x = 960
bpy.context.scene.render.resolution_y = 540

# 6. Executa o render e salva a imagem
bpy.ops.render.render(write_still=True)
print("Render concluído no Blender!")