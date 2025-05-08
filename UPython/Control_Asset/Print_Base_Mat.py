import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

target_path = '/Game/CineProps/Asset/Material/MM/M_UV.M_UV'

for asset in selected_assets:
    if isinstance(asset, unreal.MaterialInstance):
        base_material = asset.get_editor_property('parent')

        if base_material and base_material.get_path_name() == target_path:
            print(asset)

