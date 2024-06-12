import unreal

# 선택한 모든 에셋을 가져옴
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

start_num = 1

for asset in selected_assets:
    # 에셋의 경로 가져오기
    asset_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)
    folder_path = "/".join(asset_path.split("/")[:-1])
    new_asset_name = "Test_{:03d}".format(start_num)

    start_num += 1

    # 새로운 에셋 경로 생성
    new_asset_path = folder_path + "/" + new_asset_name

    # 에셋 이름 변경 및 패스 지정
    unreal.EditorAssetLibrary.rename_loaded_asset(asset, new_asset_path)

