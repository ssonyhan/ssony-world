

import unreal

def print_referencers_of_selected_assets():
    # 콘텐츠 브라우저에서 선택한 에셋 가져오기
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    
    if not selected_assets:
        unreal.log("No assets selected.")
        return
    
    for asset in selected_assets:
        # 에셋의 풀 패스 ("/Game/폴더/에셋.에셋") 얻기
        asset_full_path = asset.get_path_name()
        
        # 다른 에셋 중에서 이 에셋을 참조하고 있는 패키지들(바로가기)을 찾기
        referencer_packages = unreal.EditorAssetLibrary.find_package_referencers_for_asset(
            asset_full_path,
            load_assets_to_confirm=False  # True로 설정하면 참조 확인을 위해 패키지들을 로드
        )
        
        # 결과 출력
        unreal.log(f"Asset: {asset_full_path}")
        if not referencer_packages:
            pass
        else:
            for pkg in referencer_packages:
                unreal.log(f"  -> Referenced by package: {pkg}")

# 콘솔 또는 Editor Utility에서 호출 시
if __name__ == "__main__":
    print_referencers_of_selected_assets()


