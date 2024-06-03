import unreal

# 선택된 에셋 가져오기
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()


parameter_name = "UseWorldMapping"
i : list[str] = []

# 이름가져오기
for i in selected_assets:

# # 각 선택된 에셋에 대해 스칼라 파라미터 읽기
#     for asset in selected_assets:
#         asset = unreal.MaterialEditingLibrary.get_material_instance_scalar_parameter_value(asset,parameter_name)
#         print(i.get_name(), asset)      


# 각 선택된 에셋에 대해 Boolean 파라미터 읽기
    for asset in selected_assets:
        asset = unreal.MaterialEditingLibrary.get_material_instance_static_switch_parameter_value( asset , parameter_name)
        print(i.get_name(), asset)