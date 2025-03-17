import unreal

selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in selected_actors :
    print(dir(actor))

