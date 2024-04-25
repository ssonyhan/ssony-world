# import unreal

# # get_selected_level_actors 함수를 호출하지 않고 직접 사용
# actors = unreal.EditorLevelLibrary.get_selected_level_actors()

# if len(actors) > 0:
#     actor = actors[0]
#     loc = actor.get_actor_location()
#     loc.x += 100
#     actor.set_actor_location(loc, True, True)
# else : None


# # 선택된 모든 액터 목록을 얻음
# actors = unreal.EditorLevelLibrary.get_selected_level_actors()

# # 각 액터에 대해 반복하여 위치를 이동함
# for actor in actors:
#     rot = actor.get_actor_rotation()
#     rot.yaw += 90
#     actor.set_actor_rotation(rot, True)


# import unreal
# # 같은 오브젝트 일괄 선택

# selected_asset = unreal.EditorUtilityLibrary.get_selected_assets()
# pathName = selected_asset.get_path_name()
# ref = unreal.EditorLevelLibrary.get_actor_reference()
# actors = unreal.EditorLevelLibrary.get_all_level_actors()
# for actor in actors:
#     if actor.get_name() == ref.get_name():
#         actor.select_actor(True, True)
#     else: None 


import unreal

# 현재 선택된 액터의 레퍼런스 가져오기
selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()
print(selected_actors)
#ref_actors = unreal.EditorLevelLibrary.get_actor_reference()
#print(ref_actors)