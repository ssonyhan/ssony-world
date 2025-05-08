import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for asset in selected_assets:
    if isinstance(asset, unreal.MaterialInstance):
        base_material = asset.get_editor_property('parent')
        
        if isinstance(base_material, unreal.Material):
            blend_mode = base_material.get_editor_property('blend_mode')
            
            if blend_mode == unreal.BlendMode.BLEND_MASKED:
                print(asset.get_name())
