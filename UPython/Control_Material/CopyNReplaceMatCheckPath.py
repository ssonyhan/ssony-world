# SM Actor 및 내부 ISM comp, Decal Actor, BP 내 SM Comp, ISM comp 대응 , 소스패스 같으면 패스

import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()
source_path = source_path 

editor_asset_library = unreal.EditorAssetLibrary()


# MI Copy 
def copy_material_instance(material_instance, source_path):
    material_instance_name = material_instance.get_name()
    new_path = source_path + material_instance_name

    if isinstance(material_instance, unreal.MaterialInstance) : 

        if material_instance.get_path_name().startswith(source_path):
            unreal.log(f" {material_instance_name} already exists")
            return False

        if editor_asset_library.duplicate_asset(material_instance.get_path_name(), new_path):
            unreal.log(f"Copied {material_instance_name} to {source_path}")
            return True
        
        else:
            unreal.log_error(f"Failed to copy {material_instance_name} to {source_path}")
            return False

    else :
        unreal.log_error(f"{material_instance_name} is NOT MI")
        return False

# MI Replace
def replace_material_instance(actor, material_instance, source_path):
    material_instance_name = material_instance.get_name()
    new_material_instance_path = source_path + material_instance_name + '.' + material_instance_name

    new_material_instance = unreal.EditorAssetLibrary.load_asset(new_material_instance_path)
    
    if not new_material_instance:
        unreal.log_error(f"Failed to load MI: {new_material_instance_path}")
        return
    
    # SM Actor 처리부분
    if isinstance(actor, unreal.StaticMeshActor) :
        get_smComp = actor.static_mesh_component
        for index, mat in enumerate(get_smComp.get_materials()):
            if mat == material_instance:
                get_smComp.set_material(index, new_material_instance)
                unreal.log(f"Replaced MI {material_instance_name} in SMActor {actor.get_name()}")


        #InstancedStaicMesh 처리부분
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for ismcomp in actor_components:
            if isinstance(ismcomp, unreal.InstancedStaticMeshComponent):
                for index, mat in enumerate(ismcomp.get_materials()):
                    if mat == material_instance :
                        ismcomp.set_material(index,new_material_instance)
                        unreal.log(f"Replaced MI {material_instance_name} in InstancedSM {actor.get_name()}")


               
    # BP Actor 처리부분
    elif isinstance(actor.get_class(), unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for comp in actor_components:
            # 내뷰 SMComp 및 ISMComp 처리
            if isinstance(comp, unreal.StaticMeshComponent) or isinstance(comp, unreal.InstancedStaticMeshComponent) :
                for index, mat in enumerate(comp.get_materials()):
                    if mat == material_instance:
                        comp.set_material(index, new_material_instance)
                        unreal.log(f"Replaced MI {material_instance_name} in Blueprint {actor.get_name()}")




    # Deacal Actor 처리부분
    elif isinstance(actor, unreal.DecalActor) :
            decal_comp = actor.decal
            mat = decal_comp.get_decal_material()
            if mat == material_instance:
                decal_comp.set_decal_material(new_material_instance)
                unreal.log(f"Replaced MI {material_instance_name} in DecalActor {actor.get_name()}")


# path확인 부분
def process_material_instance(actor, material_instance, source_path):
    if not material_instance.get_path_name().startswith(source_path):  # source_path에 없으면 복사 및 교체
        if copy_material_instance(material_instance, source_path):
            replace_material_instance(actor, material_instance, source_path)
    else:
        pass




for actor in selected_assets:
    actor_class = actor.get_class()

    # SM Actor 대응 
    if isinstance(actor, unreal.StaticMeshActor) :
        get_smComp = actor.static_mesh_component

        for get_mi in get_smComp.get_materials():
            if get_mi is not None:
                process_material_instance(actor, get_mi, source_path)


        # ISM 대응
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for ismcomp in actor_components:
                if isinstance(ismcomp, unreal.InstancedStaticMeshComponent):
                    for get_mi in ismcomp.get_materials():
                        if get_mi is not None :
                            process_material_instance(actor, get_mi, source_path)
                

    # BP내 SMComp 대응 InstancedSMComp 대응
    elif isinstance(actor_class, unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)

        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent) or isinstance(comp, unreal.InstancedStaticMeshComponent) :
                for get_mi in comp.get_materials():
                    if get_mi is not None:
                        process_material_instance(actor, get_mi, source_path)

    # DecalActor 대응
    elif isinstance(actor, unreal.DecalActor):
        decal_comp = actor.decal
        mat = decal_comp.get_decal_material()
        if mat is not None:
            process_material_instance(actor, get_mi, source_path)