
import unreal

selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in selected_actors:
    # 액터의 Primitive Component를 가져옵니다 (예: Static Mesh Component)
    components = actor.get_components_by_class(unreal.PrimitiveComponent)
    
    for component in components:
        print ( actor.get_actor_label(), ">> Collision Presets <<" ,component.get_collision_profile_name()) #콜리전 프리셋 프린트 Default = BlockAll
        print ( actor.get_actor_label(), ">> Collision Enabled <<" ,component.get_collision_enabled())
        print ( actor.get_actor_label(), ">> Object Tpye<<" ,component.get_collision_object_type())

        print("--------------------------------------------------------------------------------------------")

        for compcolchannel in unreal.CollisionChannel:
            response_type = component.get_collision_response_to_channel(compcolchannel)
            print("CollisionChannel: {}, responseChannel: {}".format( compcolchannel, response_type)) 


 



 


