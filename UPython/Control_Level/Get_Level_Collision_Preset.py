
import unreal

selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in selected_actors:
    # 액터의 Primitive Component를 가져옵니다 (예: Static Mesh Component)
    components = actor.get_components_by_class(unreal.PrimitiveComponent)
    
    for component in components:
        print ( actor.get_actor_label(), ">> Collision Presets <<" ,component.get_collision_profile_name())

        