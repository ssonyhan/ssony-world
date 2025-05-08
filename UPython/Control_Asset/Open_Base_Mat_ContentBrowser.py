import unreal

def open_base_materials_from_selection():
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    
    base_materials = []
    
    for asset in selected_assets:
        if isinstance(asset, unreal.MaterialInstance):  # MI만 처리
            base_material = asset.get_base_material()
            if base_material and base_material not in base_materials:
                base_materials.append(base_material)
    
    if base_materials:
        asset_tools.open_editor_for_assets(base_materials)
    else:
        unreal.log("No valid Material Instances selected.")

open_base_materials_from_selection()
