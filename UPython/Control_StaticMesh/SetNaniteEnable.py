# Nanite On 시키는 코드

import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()


# For문 쓰는 이유 : 위의 selected_asset들은 array로 반환되기 때문에 for문을 사용하여 각각의 asset의 list를 가져와야 한다. 
# 리스트의 피처를 가져오기 위해서는 하나씩 가져와야 한다. array로 가져오면 에러가 발생한다.

for nanitemesh in selected_assets : 
    meshNaniteSettings : bool = nanitemesh.get_editor_property('nanite_settings')
    
    meshNaniteSettings.enabled = False
    print(meshNaniteSettings.enabled)
    