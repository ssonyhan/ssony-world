//SceneColor => PostProcessInput0
// Strength, LuminanceWeight => float

float2 SceneUV = GetSceneTextureUV(Parameters);
float2 TexelScale = View.BufferSizeAndInvSize.zw;

//주변 8개 픽셀의 색상 샘플링
half3 C1 = SceneTextureLookup(SceneUV + float2(-1, 0) * TexelScale, 14, false).rgb;
half3 C2 = SceneTextureLookup(SceneUV + float2(0, -1) * TexelScale, 14, false).rgb;
half3 C3 = SceneTextureLookup(SceneUV + float2(1, 0) * TexelScale, 14, false).rgb;
half3 C4 = SceneTextureLookup(SceneUV + float2(0, 1) * TexelScale, 14, false).rgb;
half3 C5 = SceneTextureLookup(SceneUV + float2(-1, -1) * TexelScale, 14, false).rgb;
half3 C6 = SceneTextureLookup(SceneUV + float2(1, -1) * TexelScale, 14, false).rgb;
half3 C7 = SceneTextureLookup(SceneUV + float2(1, 1) * TexelScale, 14, false).rgb;
half3 C8 = SceneTextureLookup(SceneUV + float2(-1, 1) * TexelScale, 14, false).rgb;

//중앙 및 주변 픽셀의 Luminance(밝기) 계산
half A0 = Luminance(SceneColor);
half CL1 = Luminance(C1);
half CL2 = Luminance(C2);
half CL3 = Luminance(C3);
half CL4 = Luminance(C4);
half CL5 = Luminance(C5);
half CL6 = Luminance(C6);
half CL7 = Luminance(C7);
half CL8 = Luminance(C8);

//Luminance 기반의 엣지 감지
half L1 = ((max(CL1, A0)) / (min(CL1, A0)) - 1);
half L2 = ((max(CL2, A0)) / (min(CL2, A0)) - 1);
half L3 = ((max(CL3, A0)) / (min(CL3, A0)) - 1);
half L4 = ((max(CL4, A0)) / (min(CL4, A0)) - 1);
half L5 = ((max(CL5, A0)) / (min(CL5, A0)) - 1);
half L6 = ((max(CL6, A0)) / (min(CL6, A0)) - 1);
half L7 = ((max(CL7, A0)) / (min(CL7, A0)) - 1);
half L8 = ((max(CL8, A0)) / (min(CL8, A0)) - 1);

half NeighborDifference = max(max(max(L1, L2), max(L3, L4)), max(max(L5, L6), max(L7, L8)));
half SharpenMask = 1.0f - clamp(NeighborDifference, 0.0f, LuminanceWeight);
SharpenMask *= SharpenMask * SharpenMask;

// Sharpen
half SharpenWeight = Strength * SharpenMask;
half4 LuminanceNeightbors = half4(CL1, CL2, CL3, CL4);
half4 LuminanceNeightbors2 = half4(CL5, CL6, CL7, CL8);
half4 A0LuminanceNeightbors = abs(A0 - LuminanceNeightbors);
half4 A0LuminanceNeightbors2 = abs(A0 - LuminanceNeightbors2);
half A0Max = max(max(A0LuminanceNeightbors.r, A0LuminanceNeightbors.g), max(A0LuminanceNeightbors.b, A0LuminanceNeightbors.a));
half A0Max2 = max(max(A0LuminanceNeightbors2.r, A0LuminanceNeightbors2.g), max(A0LuminanceNeightbors2.b, A0LuminanceNeightbors2.a));
half HDREdge = max(A0Max, A0Max2);
half EdgeMask = saturate(1.0f - HDREdge);
half LerpFactor = -EdgeMask * SharpenWeight;

// --- 코드 수정 부분 시작 ---

// 기존: half3 DeltaColor = (C1 + C2 + C3 + C4 + C5 + C6 + C7 + C8) - SceneColor * 8;
// 수정: RGB 채널 대신, 미리 계산된 Luminance 값을 사용하여 밝기 차이(Delta)를 계산합니다.
// 이렇게 하면 연산 결과가 색상 벡터(half3)가 아닌 단일 스칼라 값(half)이 됩니다.
half DeltaLuminance = (CL1 + CL2 + CL3 + CL4 + CL5 + CL6 + CL7 + CL8) - A0 * 8;

// 기존: SceneColor.rgb += DeltaColor * LerpFactor;
// 수정: 계산된 밝기 차이(DeltaLuminance)를 원본 SceneColor의 모든 채널에 동일하게 더해줍니다.
// 이렇게 하면 색조 변화 없이 밝기만 조절되어 선명해집니다.
SceneColor.rgb += DeltaLuminance * LerpFactor;

// --- 코드 수정 부분 끝 ---

return SceneColor;