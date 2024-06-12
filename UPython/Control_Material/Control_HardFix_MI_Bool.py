import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()



for asset in selected_assets :
    

    # 파라미터 및 
    parameter_name = "EnableUDW"
    control_bool_val = False
    
    if isinstance(asset, unreal.MaterialInstanceConstant):

        
        found = unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value(asset, parameter_name, control_bool_val)
        
        #업데이트 해놔야 컨텐츠 브라우저에서 저장먹힘 이거 안하면 저장안됨
        unreal.MaterialEditingLibrary.update_material_instance(asset)
        print( asset.get_name(), ">>", parameter_name, ">>>", control_bool_val )

        






    else:
        pass

