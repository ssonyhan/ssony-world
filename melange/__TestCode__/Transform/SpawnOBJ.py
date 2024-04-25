import unreal
def get_viewport_camera():
    viewport_cam_info = unreal.EditorLevelLibrary.get_level_viewport_camera_info()
    return viewport_cam_info
viewport_camera_info = get_viewport_camera()
if viewport_camera_info:
    # 카메라의 위치 정보를 가져옴
    camera_position = viewport_camera_info[0]
    # 카메라의 회전 정보를 가져옴
    camera_rotation = viewport_camera_info[1]
    # 카메라의 회전 정보를 기반으로 앞쪽을 가리키는 회전된 방향 벡터를 계산
    forward_vector = unreal.Vector(1, 0, 0).rotate_angle_axis(camera_rotation.yaw, unreal.Vector(0, 0, 1))
    # 카메라의 Pitch와 Roll 값을 기준으로 하는 UP 벡터를 계산
    up_vector = unreal.Vector(0, 0, 1).rotate_angle_axis(camera_rotation.pitch, forward_vector)
    # 이동할 거리 설정
    offset_distance = 1000.0
    # 이동할 거리만큼 앞으로 이동한 위치 계산
    spawn_position = camera_position + forward_vector * offset_distance
    # ddd 블루프린트 클래스 로드
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/ddd')
    if actor_class:
        # 첫 번째 ddd 블루프린트 생성
        ddd_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, spawn_position, camera_rotation)
        unreal.log("First ddd Blueprint spawned in front of the viewport camera.")
        if ddd_actor:
            print("dd")
            # 두 번째 ddd 블루프린트 생성 및 첫 번째 블루프린트에 연결
            ddd_actor2 = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, spawn_position, camera_rotation)
            ddd_actor2.attach_to_actor(ddd_actor, unreal.Name(), unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD)
            ddd_actor2.set_actor_relative_location((offset_distance,0,0),False,False)
            unreal.EditorLevelLibrary.destroy_actor(ddd_actor)
            unreal.log("Second ddd Blueprint spawned and attached to the first one.")
        else:
            unreal.log_warning("Failed to spawn second ddd blueprint.")
    else:
        unreal.log_warning("Failed to load ddd blueprint class.")
else:
    unreal.log_warning("No viewport camera found.")