# Nanite On 시키는 코드

import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()


for nanitemesh in selected_assets : 
    meshNaniteSettings : bool = nanitemesh.get_editor_property('nanite_settings')
    
    
    if meshNaniteSettings.enabled == True :

    
        if meshNaniteSettings.preserve_area == False :
            meshNaniteSettings.preserve_area = True
            print('Preserve Area On')
        
        else :
            meshNaniteSettings.preserve_area = False
            print('Preserve Area Off')
    else :
        print('Turn On Nanite')