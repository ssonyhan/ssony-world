
import unreal

# 선택한 에셋을 가져옴
clicked_assets = unreal.EditorUtilityLibrary.get_selected_assets()
pathes: list[str] = []
for asset in clicked_assets:
    assetpath = asset.get_path_name()
    # print(assetpath)
    splitpath = assetpath.split("/")[0:-1]
    # print(splitpath)
    resultpath = "/".join(splitpath)
    print(resultpath)

print("------------------------------------------------------")
