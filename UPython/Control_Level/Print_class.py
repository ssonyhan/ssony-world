import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()


for asset in selected_assets :
    if isinstance(asset, unreal.CinevCharacter) :
        print(asset.get_name(),">>" ,asset.get_actor_label(), ">>>", asset.__class__)