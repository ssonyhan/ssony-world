import unreal

actors = unreal.EditorLevelLibrary.get_all_level_actors()

for actor in actors:
    components = actor.get_components_by_class(unreal.MeshComponent)

    for comp in components:
        material_count = comp.get_num_materials()

        for idx in range(material_count):
            material_interface = comp.get_material(idx)

            if material_interface:
                # get_base_material() 호출
                base_material = material_interface.get_base_material()
                print(f"{actor.get_name()} - Slot {idx} Base Material: {base_material.get_name()}")
                unreal.AssetToolsHelpers.get_asset_tools().open_editor_for_assets([base_material])


