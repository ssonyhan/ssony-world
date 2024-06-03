import unreal

# 선택된 에셋 가져오기
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# 각 선택된 에셋에 대해 파라미터 읽기
for asset in selected_assets:
    if isinstance(asset, unreal.MaterialInstance):
        material_instance = asset
        
        # 파라미터 딕셔너리 생성
        parameters = {
            "scalar": {},
            "vector": {},
            "texture": {}
        }

        # Scalar 파라미터 읽기
        scalar_params = material_instance.get_editor_property('scalar_parameter_values')
        for param in scalar_params:
            parameters["scalar"][param.parameter_info.name] = param.parameter_value

        # Vector 파라미터 읽기
        vector_params = material_instance.get_editor_property('vector_parameter_values')
        for param in vector_params:
            parameters["vector"][param.parameter_info.name] = param.parameter_value

        # Texture 파라미터 읽기
        texture_params = material_instance.get_editor_property('texture_parameter_values')
        for param in texture_params:
            parameters["texture"][param.parameter_info.name] = param.parameter_value


        print(f"{material_instance.get_name()}: {parameters}")
    else:
        print(f"{asset.get_name()} is not a MaterialInstance.")