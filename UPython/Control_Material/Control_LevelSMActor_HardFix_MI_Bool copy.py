# 레벨의 SM Actor에 Material element 갯수가 1개라면 내부에 있는 파라미터 값 하드 픽스

import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()



for actor in selected_assets :

    actor_class = actor.get_class()


    # SM Actor 대응
    if isinstance(actor, unreal.StaticMeshActor) :

        get_smComp = actor.static_mesh_component
        get_mi_array = get_smComp.get_materials()
        mi_len = len(get_mi_array)

        if mi_len == 1 :

            get_mi_0 = get_smComp.get_material(0)

            # 파라미터 이름 및 수치
            parameter_name = "EnableUDW"
            control_bool_val = False

            changeval = unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value(get_mi_0, parameter_name, control_bool_val)
            unreal.MaterialEditingLibrary.update_material_instance(get_mi_0)

            print(actor.get_name(), ">", get_mi_0.get_name(), ">>", parameter_name, ">>>", control_bool_val)

        else :
            print(">>Material is more than 1 <<")



    else :
        print("Not SM")

 




    

