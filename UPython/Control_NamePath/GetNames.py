import unreal

SelectedAsset = unreal.EditorUtilityLibrary.get_selected_assets()
# print(SelectedAsset)


i : list[str] = []

for i in SelectedAsset:
    print(i.get_name())

