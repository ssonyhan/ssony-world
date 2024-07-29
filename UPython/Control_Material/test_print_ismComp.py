import unreal
selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()


for actor in selected_assets:
    if isinstance(actor, unreal.StaticMeshActor):
        # Actor의 모든 컴포넌트 가져오기
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        
        for comp in actor_components:
            # InstancedStaticMeshComponent인 경우
            if isinstance(comp, unreal.InstancedStaticMeshComponent):
                comp_name = comp.get_name()

                mat_len = comp.get_num_materials()

                for i in range(mat_len):
                    comp_mat = comp.get_material(i)
                    print(comp_name, '>>>>>', comp_mat)


    elif isinstance(actor.get_class(), unreal.BlueprintGeneratedClass) :
        actor_components = actor.get_components_by_class(unreal.ActorComponent)

        for comp in actor_components:
          
            if isinstance(comp, unreal.StaticMeshComponent) or isinstance(comp, unreal.InstancedStaticMeshComponent) :
                print(comp.get_name(),'>>>>')



    else:
        pass




    