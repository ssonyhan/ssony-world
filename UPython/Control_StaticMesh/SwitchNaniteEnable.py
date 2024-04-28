# Nanite On 시키는 코드

import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()


for nanitemesh in selected_assets : 
    meshNaniteSettings : bool = nanitemesh.get_editor_property('nanite_settings')
    
    if meshNaniteSettings.enabled == True :
        meshNaniteSettings.enabled = False
        print("Nanite Off")
    else :
        meshNaniteSettings.enabled = True
        print("Nanite On")
