# 폴더의 에셋의 레퍼런스 확인

import unreal 


def unused_asset_notifier(workingPath : str) -> list[str]:
    need_to_return = []
    @unreal.uclass()
    class GetEditorAssetLibrary(unreal.EditorAssetLibrary):
        pass

    editorAssetLib = GetEditorAssetLibrary()

    allAssets = editorAssetLib.list_assets(workingPath, True, False)

    if (len(allAssets) > 0):
        for asset in allAssets:
            deps = editorAssetLib.find_package_referencers_for_asset(asset, False)
            if (len(deps) == 0):
                print (">>>%s" % asset)
                need_to_return.append(asset)



    return need_to_return



unused = unused_asset_notifier('/Game/FX/Texture/')