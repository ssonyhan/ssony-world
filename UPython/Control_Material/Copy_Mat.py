#레벨에 있는 머트리얼 인스턴스 긁어서 destination_path 경로에 복사하기

import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()

destination_path = '/Game/TA/Users/ssony/0_mat'
editor_asset_library = unreal.EditorAssetLibrary()

# MI Copy
def copy_material_instance(material_instance, destination_path):
    material_instance_name = material_instance.get_name()
    new_path = destination_path + material_instance_name
    if editor_asset_library.duplicate_asset(material_instance.get_path_name(), new_path):
        unreal.log(f"Copied {material_instance_name} to {destination_path}")
    else:
        unreal.log_error(f"Failed to copy {material_instance_name} to {destination_path}")



for actor in selected_assets:
    actor_class = actor.get_class()

    # SM Actor 대응
    if isinstance(actor, unreal.StaticMeshActor):
        get_smComp = actor.static_mesh_component

        for get_mi in get_smComp.get_materials():
            if get_mi is not None:
                copy_material_instance(get_mi, destination_path)

    # BP 대응
    elif isinstance(actor_class, unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)

        for Comp in actor_components:
            if isinstance(Comp, unreal.StaticMeshComponent):
                for get_mi in Comp.get_materials():
                    if get_mi is not None:
                        copy_material_instance(get_mi, destination_path)

    
