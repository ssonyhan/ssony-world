#MI Depth 정리용


import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for each in selected_assets :
    print(each.get_name())
    if each.__class__ == unreal.MaterialInstanceConstant :

        get_parent_mat = each.get_editor_property('parent')
        get_Master_mat = each.get_base_material()

        if get_parent_mat.__class__ == unreal.MaterialInstanceConstant :

            set_Master_mat = each.set_editor_property('parent',get_Master_mat)
            print("Set Base Mat")

        else :
            pass

    else :
        print("Not MaterialInstance")
