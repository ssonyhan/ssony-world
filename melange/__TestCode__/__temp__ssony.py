import unreal, importlib
from Lib import __lib_archeron__ as archeron

importlib.reload(archeron)

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
selected_asset = selected_assets[0]
pathName = selected_asset.get_path_name()
getDirectoryPath = pathName.split("/")[0:-1]
gatherPath = "/".join(getDirectoryPath)
# print(gatherPath)
   