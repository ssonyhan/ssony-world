import unreal


selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for each in selected_assets :
    if each.__class__ == unreal.MaterialInstanceConstant :

        get_parent_mat = each.get_editor_property('parent')

        if get_parent_mat.__class__ == unreal.MaterialInstanceConstant :
            print(each.get_name())
            print("Have Depth")

        else :
            pass

    else :
        print("Not MaterialInstance")
