# Nanite On 시키는 코드

import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()



for nanitemesh in selected_assets : 
    meshNaniteSettings : bool = nanitemesh.get_editor_property('nanite_settings')
   
    if nanitemesh.__class__ == unreal.StaticMesh:
        materials = []
        blend_modes = []
        is_tras = []
        
    for getmaterial in range(nanitemesh.get_num_sections(0)): # 
        # get_num_sections(0)은 스태틱 메시의 섹션 수를 가져오는 함수. (0)= LOD 
        # 스태틱 메시의 LOD에 대한 정보를 가져오기 위한 인덱스입니다.
        material = nanitemesh.get_material(getmaterial)
        materials.append(material)
        blend_modes.append(material.get_blend_mode())
        

    for blend_mode in blend_modes:
        if blend_mode == unreal.BlendMode.BLEND_TRANSLUCENT:
                is_tras.append(True)
        else :
                is_tras.append(False)

    
if any(is_tras):
    meshNaniteSettings.enabled = False
    print("is translucent")
            
else:
    meshNaniteSettings.enabled = True
    print("nanite On")

