import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in selected_assets :


    # SM Actor
    if isinstance(actor, unreal.StaticMeshActor) :
        get_smComp = actor.static_mesh_component
        for index, get_sm_mm in enumerate(get_smComp.get_materials()):
            if isinstance(get_sm_mm, unreal.Material) :
                print(actor.get_actor_label(),">>>>", '<',index, '>', get_sm_mm.get_name())
        
        actor_components = actor.get_components_by_class(unreal.ActorComponent)    
        for ismcomp in actor_components:
            if isinstance(ismcomp, unreal.InstancedStaticMeshComponent):
                for index, get_ism_mm in enumerate(ismcomp.get_materials()):
                    if isinstance(get_ism_mm, unreal.Material):
                        print(actor.get_actor_label(),">>>", ismcomp.get_name(),">>>>",'<',index, '>', get_ism_mm.get_name())



    # BP Actor   
    elif isinstance(actor.get_class(), unreal.BlueprintGeneratedClass) : 
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent) or isinstance(comp, unreal.InstancedStaticMeshComponent) :
                for index, get_comp_mm in enumerate(comp.get_materials()) :
                    if isinstance(get_comp_mm, unreal.Material):
                        print(actor.get_actor_label(),">>>", comp.get_name(), ">>>>",'<',index, '>', get_comp_mm.get_name())


    
    # Decal Actor
    elif isinstance(actor, unreal.DecalActor) :
        decal_comp = actor.decal
        get_decal_mm = decal_comp.get_decal_material()
        if isinstance(get_decal_mm, unreal.Material):
            print(actor.get_actor_label(),">>>>",'<',index, '>', get_decal_mm.get_name())


    else:
        pass