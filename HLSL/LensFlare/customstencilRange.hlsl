

float RangeCheck = (B >= B && B <= B + MaxRange ) ? 1.0 : 0.0;

// 2단계: A와 B를 비교해서 조건에 따라 결과 반환
float Result = (RangeCheck == 1.0 && A == B) ? 1.0 : 0.0;

return Result;


if((int)stencil == 0)
{
    return SceneColor;
} 
else 
{
    return (float3) 1;
}

////////////////////////////////////

if((int)stencil == customindex )
{
    return SceneColor;
} 
else 
{
    return (float3) 1;
}




float StencilValue = SceneTextureLookup(UV, PPI_CustomStencil).r;

if (StencilValue == 30.0) {
    // Stencil 값이 30일 경우
    return float3(1.0, 1.0, 1.0); // 흰색 반환
} else if (StencilValue > 30.0) {
    // Stencil 값이 30보다 클 경우
    return SceneTextureLookup(UV, PPI_PostProcessInput0).rgb; // PostProcessInput0 값을 반환
} else if (StencilValue < 30.0) {
    // Stencil 값이 30보다 작을 경우
    return float3(0.0, 0.0, 0.0); // 검정색 반환
} else {
    // 기본값
    return float3(0.5, 0.5, 0.5); // 중간 회색 반환
}