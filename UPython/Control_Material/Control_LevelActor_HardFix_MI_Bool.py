import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in selected_assets:

    actor_class = actor.get_class()

    # 파라미터 이름 및 수치
    parameter_name = "sss"
    control_bool_val = True

    # SM Actor 대응
    if isinstance(actor, unreal.StaticMeshActor):
        get_smComp = actor.static_mesh_component

        for get_mi in get_smComp.get_materials():

            if get_mi is not None:

                get_mi_param = unreal.MaterialEditingLibrary.get_static_switch_parameter_source(get_mi,parameter_name)

                if get_mi_param :
                    changeval = unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value(get_mi, parameter_name, control_bool_val)
                    unreal.MaterialEditingLibrary.update_material_instance(get_mi)
                    print(actor.get_name(), ">", get_mi.get_name(), ">>", parameter_name, ">>>", control_bool_val)
                else :
                    print(actor.get_name(), ">", get_mi.get_name(), ">>", parameter_name, ">>> 해당 파라미터는 존재하지 않습니다")

    # BP대응
    elif isinstance(actor_class, unreal.BlueprintGeneratedClass):

        actor_components = actor.get_components_by_class(unreal.ActorComponent)

        for Comp in actor_components:
            if isinstance(Comp, unreal.StaticMeshComponent):
                for get_mi in Comp.get_materials():

                    if get_mi is not None:

                        get_mi_param = unreal.MaterialEditingLibrary.get_static_switch_parameter_source(get_mi,parameter_name)

                        
                        if get_mi_param:
                            changeval = unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value(get_mi, parameter_name, control_bool_val)
                            unreal.MaterialEditingLibrary.update_material_instance(get_mi)
                            print(actor.get_name(), ">", get_mi.get_name(), ">>", parameter_name, ">>>", control_bool_val)
                        else:
                            print(actor.get_name(), ">", get_mi.get_name(), ">>", parameter_name, ">>> 해당 파라미터는 존재하지 않습니다")

    else:
        print("Not SM")