
'''
# SM Actor, Decal Actor 대응 

import unreal

# SM Actor, BP 내 SM Actor, Decal Actor

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()
source_path = '/Game/TA/Users/ssony/0_mat/'

editor_asset_library = unreal.EditorAssetLibrary()

# MI Copy
def copy_material_instance(material_instance, source_path):
    material_instance_name = material_instance.get_name()
    new_path = source_path + material_instance_name
    if editor_asset_library.duplicate_asset(material_instance.get_path_name(), new_path):
        unreal.log(f"Copied {material_instance_name} to {source_path}")
        
    else:
        unreal.log_error(f"Failed to copy {material_instance_name} to {source_path}")

# MI Replace
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

    elif isinstance(actor, unreal.DecalActor)

    elif isinstance(actor.get_class(), unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent):
                for index, mat in enumerate(comp.get_materials()):
                    if mat == material_instance:
                        comp.set_material(index, new_material_instance)
                        unreal.log(f"Replaced material instance {material_instance_name} in Blueprint {actor.get_name()}")

for actor in selected_assets:
    actor_class = actor.get_class()

    # StaticMeshActor 대응
    if isinstance(actor, unreal.StaticMeshActor):
        get_smComp = actor.static_mesh_component

        for get_mi in get_smComp.get_materials():
            if get_mi is not None:
                copy_material_instance(get_mi, source_path)
                replace_material_instance(actor, get_mi, source_path)

    # Blueprint 대응
    elif isinstance(actor_class, unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)

        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent):
                for get_mi in comp.get_materials():
                    if get_mi is not None:
                        copy_material_instance(get_mi, source_path)
                        replace_material_instance(actor, get_mi, source_path)

'''





'''
# SM Actor, Decal Actor, BP 내 SM Comp 대응 

import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()
source_path = '/Game/TA/Users/ssony/0_mat/'

editor_asset_library = unreal.EditorAssetLibrary()

# MI Copy
def copy_material_instance(material_instance, source_path):
    material_instance_name = material_instance.get_name()
    new_path = source_path + material_instance_name
    if editor_asset_library.duplicate_asset(material_instance.get_path_name(), new_path):
        unreal.log(f"Copied {material_instance_name} to {source_path}")
    else:
        unreal.log_error(f"Failed to copy {material_instance_name} to {source_path}")

# MI Replace
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

    elif isinstance(actor, unreal.DecalActor) :
            decal_comp = actor.decal
            mat = decal_comp.get_decal_material()
            if mat == material_instance:
                decal_comp.set_decal_material(new_material_instance)
                unreal.log(f"Replaced material instance {material_instance_name} in DecalActor {actor.get_name()}")



for actor in selected_assets:
    actor_class = actor.get_class()

    # SM Actor 대응
    if isinstance(actor, unreal.StaticMeshActor):
        get_smComp = actor.static_mesh_component

        for get_mi in get_smComp.get_materials():
            if get_mi is not None:
                copy_material_instance(get_mi, source_path)
                replace_material_instance(actor, get_mi, source_path)

    # BP내 SMComp 대응
    elif isinstance(actor_class, unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)

        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent):
                for get_mi in comp.get_materials():
                    if get_mi is not None:
                        copy_material_instance(get_mi, source_path)
                        replace_material_instance(actor, get_mi, source_path)

    # DecalActor 대응
    elif isinstance(actor, unreal.DecalActor):
        decal_comp = actor.decal
        mat = decal_comp.get_decal_material()
        if mat is not None:
            copy_material_instance(mat, source_path)
            replace_material_instance(actor, mat, source_path)


'''


# SM Actor및 내부 Instance SM , Decal Actor, BP 내 SM Comp, Instance SM  대응 

import unreal

selected_assets = unreal.EditorLevelLibrary.get_selected_level_actors()
source_path = source_path

editor_asset_library = unreal.EditorAssetLibrary()

# MI Copy
def copy_material_instance(material_instance, source_path):
    material_instance_name = material_instance.get_name()
    new_path = source_path + material_instance_name
    if editor_asset_library.duplicate_asset(material_instance.get_path_name(), new_path):
        unreal.log(f"Copied {material_instance_name} to {source_path}")
    else:
        unreal.log_error(f"Failed to copy {material_instance_name} to {source_path}")

# MI Replace
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
        
        # Check for InstancedStaticMeshComponent inside StaticMeshActor
        for comp in actor.get_components_by_class(unreal.InstancedStaticMeshComponent):
            for index, mat in enumerate(comp.get_materials()):
                if mat == material_instance:
                    comp.set_material(index, new_material_instance)
                    unreal.log(f"Replaced material instance {material_instance_name} in InstancedStaticMeshComponent of StaticMeshActor {actor.get_name()}")

    elif isinstance(actor.get_class(), unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)
        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent) or isinstance(comp, unreal.InstancedStaticMeshComponent):
                for index, mat in enumerate(comp.get_materials()):
                    if mat == material_instance:
                        comp.set_material(index, new_material_instance)
                        unreal.log(f"Replaced material instance {material_instance_name} in Blueprint {actor.get_name()}")

    elif isinstance(actor, unreal.DecalActor):
        decal_comp = actor.decal
        mat = decal_comp.get_decal_material()
        if mat == material_instance:
            decal_comp.set_decal_material(new_material_instance)
            unreal.log(f"Replaced material instance {material_instance_name} in DecalActor {actor.get_name()}")

for actor in selected_assets:
    actor_class = actor.get_class()

    # SM Actor 대응
    if isinstance(actor, unreal.StaticMeshActor):
        get_smComp = actor.static_mesh_component

        for get_mi in get_smComp.get_materials():
            if get_mi is not None:
                copy_material_instance(get_mi, source_path)
                replace_material_instance(actor, get_mi, source_path)
        
        # Check for InstancedStaticMeshComponent inside StaticMeshActor
        for comp in actor.get_components_by_class(unreal.InstancedStaticMeshComponent):
            for get_mi in comp.get_materials():
                if get_mi is not None:
                    copy_material_instance(get_mi, source_path)
                    replace_material_instance(actor, get_mi, source_path)

    # BP내 SMComp 및 InstancedSMComp 대응
    elif isinstance(actor_class, unreal.BlueprintGeneratedClass):
        actor_components = actor.get_components_by_class(unreal.ActorComponent)

        for comp in actor_components:
            if isinstance(comp, unreal.StaticMeshComponent) or isinstance(comp, unreal.InstancedStaticMeshComponent):
                for get_mi in comp.get_materials():
                    if get_mi is not None:
                        copy_material_instance(get_mi, source_path)
                        replace_material_instance(actor, get_mi, source_path)

    # DecalActor 대응
    elif isinstance(actor, unreal.DecalActor):
        decal_comp = actor.decal
        mat = decal_comp.get_decal_material()
        if mat is not None:
            copy_material_instance(mat, source_path)
            replace_material_instance(actor, mat, source_path)

