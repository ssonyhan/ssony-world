#레벨에 있는 머트리얼 인스턴스 긁어서 source_path에 있는 같은 이름의 MI로 대체해주기

import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()
source_path = '/Game/CineMaps/02_Office/Office/Lv_Office_Office_A_01/00_Material/'


#리플레이스 머트리얼 
def replace_material_instance(actor, material_instance, source_path):
    material_instance_name = material_instance.get_name()
    new_material_instance_path = source_path + material_instance_name + '.' + material_instance_name

    new_material_instance = unreal.EditorAssetLibrary.load_asset(new_material_instance_path)
    
    if not new_material_instance:
        unreal.log_error(f"Failed to load material instance: {new_material_instance_path}")
        return
    
    if isinstance(actor, unreal.StaticMeshActor):
        get_smComp = actor.static_mesh_component
        for index, mat in enumerate(get_smComp.get_materials()):
            if mat == material_instance:
                get_smComp.set_material(index, new_material_instance)
                unreal.log(f"Replaced material instance {material_instance_name} in StaticMeshActor {actor.get_name()}")

    elif isinstance(actor.get_class(), unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent):
                for index, mat in enumerate(comp.get_materials()):
                    if mat == material_instance:
                        comp.set_material(index, new_material_instance)
                        unreal.log(f"Replaced material instance {material_instance_name} in Blueprint {actor.get_name()}")



for actor in selected_assets:

    #SM Actor 대응
    if isinstance(actor, unreal.StaticMeshActor):
        get_smComp = actor.static_mesh_component
        for get_mi in get_smComp.get_materials():
            if get_mi is not None:
                replace_material_instance(actor, get_mi, source_path)


    #BP 대응
    elif isinstance(actor.get_class(), unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent):
                for get_mi in comp.get_materials():
                    if get_mi is not None:
                        replace_material_instance(actor, get_mi, source_path)
