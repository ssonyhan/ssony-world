// LensFlare Billboard Parametric Ghost , v1.1
// By CyberAlien 2023

// Tex -> Texture
// Step -> Float
// UV -> LensFlare_Distortion return
// Size 1.96 -> Float
// Offset -> Float
// H -> Float
// V -> Float

float3 Result = 0;
// get placement on screen
float4 ObjectPos = mul(float4(LWCToFloat(GetObjectWorldPosition(Parameters)).xyz,1),LWCToFloat(ResolvedView.WorldToClip)); // 월드 -> 스크린
float2 ObjectToScreen = float2( ((ObjectPos.xy / ObjectPos.w).x * 0.5 )+ 0.5 , (((ObjectPos.xy / ObjectPos.w).y * -0.5 ) + 0.5 )); // 스크린 -> 정규화스크린 0->1

float2 Pos = (((ObjectToScreen - float2(0.5,0.5)) * float2(-1,-1))* (Offset) ) + float2(0.5,0.5); // (0.5, 0.5)를 기준으로 중앙에 맞춘 후 offset값에 따른 좌표위치 조정
Pos = float2(lerp(0.5,Pos.x,H),lerp(0.5,Pos.y,V)); // lerp을 이용한 수평수직 보간
float2 Coord = UV * ( 1/Size.xy ) - (Pos/Size.xy) + float2(0.5,0.5); // size값에 맞춰 UV좌표 조정
float Mask = ( step( Pos.x-(Size.x/2) , UV.x )* step( UV.x , Pos.x+(Size.x/2)) ) * ( step( Pos.y-(Size.y/2) , UV.y )* step( UV.y , Pos.y+(Size.y/2) ));
//step 함수를 사용해 텍스처의 특정 영역 내에서만 렌즈 플레어를 렌더링합니다. Pos와 Size를 기준으로 사각형 범위를 설정하고, 그 안에서만 텍스처가 그려지도록 합니다.

if( Mask > 0.0001000 ) // 텍스쳐 적용
{
Result += Texture2DSample( Tex,TexSampler, Coord.xy ).xyz * Mask.x;
return Result;
}
else
{
	return 0;
}


