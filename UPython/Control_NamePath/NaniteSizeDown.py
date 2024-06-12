# import unreal #하드픽스버전
# from Lib import __lib_topaz__ as topaz

# desired_triangle_percentage : float

# selected : list = topaz.get_selected_assets() #get selected assets using editorUtilityLib

# for staticMesh in selected : 
#     meshNaniteSettings : bool = staticMesh.get_editor_property('nanite_settings')
#     blendModes = topaz.get_materials_from_staticmesh(staticMesh, True)
#     is_translucent_exist = topaz.is_translucent_exist(blendModes)
#     if meshNaniteSettings.enabled == False and not is_translucent_exist : 
#         meshNaniteSettings.enabled = True # On nanite setting 
#         unreal.StaticMeshEditorSubsystem().set_nanite_settings(staticMesh,meshNaniteSettings, apply_changes=True) #apply changes
#         print('Nanite is Enabled')
#     else :
#         print('Nanite is already Enabled or this static mesh contains translucent material.')





'''
import unreal # 기존 설정값보다 값이 작을때만 적용되도록 수정
from Lib import __lib_topaz__ as topaz


desired_triangle_percentage : float

assets = topaz.get_selected_assets()
## execution here ##
for each in assets :
                
    if each.__class__ == unreal.StaticMesh : 
        if each is not None : 

            nanite_settings : unreal.MeshNaniteSettings     = each.get_editor_property('nanite_settings')
            nanite_settings.enabled = True

            getTrianglePercent = nanite_settings.get_editor_property('keep_percent_triangles')

            if getTrianglePercent >= desired_triangle_percentage :
                nanite_settings.keep_percent_triangles = desired_triangle_percentage 
                each.set_editor_property('nanite_settings', nanite_settings)

            else : # getTrianglePercent < desired_triangle_percentage 
                pass
 
print('OK')
'''



import unreal #트렌수클런트가 있는지 확인하는 함수 추가
from Lib import __lib_topaz__ as topaz
import importlib


importlib.reload(topaz)

desired_triangle_percentage : float = 0.33

assets = topaz.get_selected_assets()
## execution here ##
for each in assets :

    blendModes = topaz.get_materials_from_staticmesh(each, True)
    is_translucent_exist = topaz.is_translucent_exist(blendModes)

                
    if each.__class__ == unreal.StaticMesh : 
        if not is_translucent_exist :
            if each is not None : 
                nanite_settings : unreal.MeshNaniteSettings     = each.get_editor_property('nanite_settings')
                nanite_settings.enabled = True


                getTrianglePercent = nanite_settings.get_editor_property('keep_percent_triangles')

                if getTrianglePercent >= desired_triangle_percentage :
                    nanite_settings.keep_percent_triangles = desired_triangle_percentage 
                    each.set_editor_property('nanite_settings', nanite_settings)
                    unreal.StaticMeshEditorSubsystem().set_nanite_settings(each, nanite_settings, apply_changes=True)

                else : # getTrianglePercent < desired_triangle_percentage 
                    pass
 
print('OK')








