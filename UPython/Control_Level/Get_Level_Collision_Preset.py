
import unreal

selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in selected_actors:
    # 액터의 Primitive Component를 가져옵니다 (예: Static Mesh Component)
    components = actor.get_components_by_class(unreal.PrimitiveComponent)
    
    for component in components:

        compcol_preset = component.get_collision_profile_name()
        compcol_enabled = component.get_collision_enabled()
        compcol_object = component.get_collision_object_type()


        compcol_enabled_str = str(compcol_enabled).replace("CollisionEnabled.", "")
        compcol_object_str = str(compcol_object).replace("CollisionChannel.ECC_", "")




        print ( actor.get_actor_label(), ">> Collision Presets <<" ,compcol_preset) #콜리전 프리셋 프린트 Default = BlockAll
        print ( actor.get_actor_label(), ">> Collision Enabled <<" , compcol_enabled_str)
        print ( actor.get_actor_label(), ">> Object Tpye<<" ,compcol_object_str)
        
        # rint ( actor.get_actor_label(), ">> Object Tpye<<" , compcol_object.value) # 뒤에 넘버링만 나옴
    



        print("--------------------------------------------------------------------------------------------")

        for compcolchannel in unreal.CollisionChannel:
            response_type = component.get_collision_response_to_channel(compcolchannel)
            print("CollisionChannel: {}, responseChannel: {}".format( compcolchannel.get_display_name(), response_type.get_display_name())) 


 



 


