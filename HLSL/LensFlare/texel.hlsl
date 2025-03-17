float2 uv = ScreenPos.xy / ScreenPos.w;          // 뷰포트 UV
float2 pixelSize = 1.0 / ScreenTextureSize;      // 한 픽셀당 UV 크기
float2 offset = RimLightThickness * pixelSize;   // 샘플링할 오프셋(가로/세로)

// 주변 3×3(9픽셀) 샘플링 (중심 포함)
float depthC  = SceneTextureLookup(uv, SceneTextureCustomDepth, false).r; 
float depthU  = SceneTextureLookup(uv + float2(0, -offset.y), SceneTextureCustomDepth, false).r;
float depthD  = SceneTextureLookup(uv + float2(0, offset.y), SceneTextureCustomDepth, false).r;
float depthL  = SceneTextureLookup(uv + float2(-offset.x, 0), SceneTextureCustomDepth, false).r;
float depthR  = SceneTextureLookup(uv + float2( offset.x, 0), SceneTextureCustomDepth, false).r;
float depthUL = SceneTextureLookup(uv + float2(-offset.x, -offset.y), SceneTextureCustomDepth, false).r;
float depthUR = SceneTextureLookup(uv + float2( offset.x, -offset.y), SceneTextureCustomDepth, false).r;
float depthDL = SceneTextureLookup(uv + float2(-offset.x, offset.y), SceneTextureCustomDepth, false).r;
float depthDR = SceneTextureLookup(uv + float2( offset.x, offset.y), SceneTextureCustomDepth, false).r;

// 합치거나 평균을 내고, 마지막에 필요한 연산을 더 수행
float sumDepth = depthC + depthU + depthD + depthL + depthR + depthUL + depthUR + depthDL + depthDR;
float avgDepth = sumDepth / 9.0;

// 질문 속 그래프에서는 'EdgesGreenDepth'를 곱하고 매우 큰 값을 나누는 식이 보이므로,
// 아래처럼 스케일링(축소/확대) 과정을 해주면 됩니다. (예: 1000000.0f 로 나누기)
float scaledDepth = (avgDepth * EdgesGreenDepth) / 1000000.0;

// 최종 출력. Custom Node가 float1을 리턴하도록 했다면 그냥 그대로 return.
// 머티리얼에서 color(예: float4)로 쓰려면 float4(scaledDepth,0,0,1) 등으로 감싸서 리턴.
return scaledDepth;