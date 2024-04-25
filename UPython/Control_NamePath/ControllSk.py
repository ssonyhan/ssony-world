import unreal
# 데이터프렙 자산 생성
# Base = "Game/Customizing/Character_New/Clothes_Re/Female/Shoes/F_Boots_003/Skinning/F_Boots_003"
selectedAssets = unreal.EditorUtilityLibrary.get_selected_assets()
selectedAsset = selectedAssets[0]
# print(selectedAsset.get_path_name)
# this is USkeletalmesh
print(selectedAsset)
#[{SkeletalMeshLODInfo}...]
lod_setting = selectedAsset.get_editor_property('lod_info')
print(lod_setting[0])
#USkeletalMeshReductionSetting
reduction_setting = lod_setting[0].get_editor_property('reduction_settings')
print(reduction_setting)
num_tri = reduction_setting.get_editor_property('num_of_triangles_percentage')
new_reduction_setting = unreal.SkeletalMeshOptimizationSettings()
new_lod_info = unreal.SkeletalMeshLODInfo()
new_reduction_setting.set_editor_property('num_of_triangles_percentage', 0.1)
new_lod_info.set_editor_property('reduction_settings',new_reduction_setting)
#new_lod_info[0] = lod_setting[0]
selectedAsset.set_editor_property('lod_info', [new_lod_info])