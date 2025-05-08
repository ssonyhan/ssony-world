import unreal

def replace_specific_base_material():
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    target_material_path = "/Game/MSPresets/M_MS_Decal_Material/M_Masked"
    source_material_path = "/Game/CineProps/Asset/Material/MM/M_Masked.M_Masked"
    
    target_material = unreal.load_asset(target_material_path)
    
    if not target_material:
        unreal.log_error(f"Failed to load target material: {target_material_path}")
        return
    
    for asset in selected_assets:
        if isinstance(asset, unreal.MaterialInstanceConstant):
            base_material = asset.get_editor_property('parent')
            
            if base_material and base_material.get_path_name() == source_material_path:
                asset.set_editor_property('parent', target_material)
                asset.post_edit_change()
                unreal.log(f"Updated {asset.get_name()} to use {target_material.get_name()}")

replace_specific_base_material()






# import unreal

# def replace_specific_base_material():

#     selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
#     target_material_path = "/Game/MSPresets/M_MS_Decal_Material/M_MS_Decal_Material.M_MS_Decal_Material"
#     target_material = unreal.load_asset(target_material_path)
    
#     for asset in selected_assets:
#         base_material = asset.get_editor_property('parent')
#         asset.set_editor_property('parent', target_material)
#         asset.post_edit_change()
#         unreal.log(f"Updated {asset.get_name()} to use {target_material.get_name()}")

# replace_specific_base_material()
