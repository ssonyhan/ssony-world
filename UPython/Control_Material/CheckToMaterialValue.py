
import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# 확인하고자 하는 파라미터 이름
parameter_name = "EnableUDW"

# get boolean parameter
for asset in selected_assets:
    if isinstance(asset, unreal.MaterialInstance):
        # 파라미터 이름과 값을 가져오기
        found = unreal.MaterialEditingLibrary.get_material_instance_static_switch_parameter_value(asset, parameter_name)
        if found:
            print(f"Asset: {asset.get_name()}", parameter_name, ">>>", found )
        else: 
            pass
    else:
        pass


# # get scalar parameter
# for asset in selected_assets:
#     if isinstance(asset, unreal.MaterialInstance):
#         found = unreal.MaterialEditingLibrary.get_material_instance_scalar_parameter_value(asset,parameter_name)
#         if found:
#             print(f"Asset: {asset.get_name()}", parameter_name, ">>>", found )
#         else: 
#             pass
#     else:
#         pass