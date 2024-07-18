'''

from Lib import __lib_topaz__ as topaz
import unreal 

temp : unreal.AnimSequence = topaz.get_selected_asset()

print(temp)

ctrl : unreal.AnimationDataController = temp.controller # 형변환

print(ctrl)


f_t0 = unreal.FrameNumber(3951) #3951
f_t1 = unreal.FrameNumber(4251) #4251 끝프레임4751
frames = unreal.FrameNumber.__sub__(f_t1, f_t0) #300

ctrl.resize_number_of_frames(frames,f_t0, f_t1)
print(frames)

'''


# API가 제대로 안돔... t0,t1무시하고 부조건 0부터 짤림
import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

start_frame = 3951
end_frame = 4251

t0 = unreal.FrameNumber(start_frame)
t1 = unreal.FrameNumber(end_frame)
frames = unreal.FrameNumber.__sub__(t1, t0)


if selected_assets:
    asset = selected_assets[-1]  # 첫 번째 선택된 에셋을 가져옴
    if isinstance(asset, unreal.AnimSequence):

        control_anim_asset : unreal.AnimationDataController = asset.controller
        print(control_anim_asset)
        print(asset)
        control_anim_asset.resize_number_of_frames(frames,t0,t1)



    else :
        print("Animation Sequence가 아닙니다.")


