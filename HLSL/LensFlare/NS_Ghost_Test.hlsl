// LensFlare Billboard Parametric Ghost , v1.1
// By CyberAlien 2023

// Tex 
// Step
// UV
// Size 
// Offset
// H
// V

float3 Result = 0;
// get placement on screen
float4 ObjectPos = mul(float4(LWCToFloat(GetObjectWorldPosition(Parameters)).xyz,1),LWCToFloat(ResolvedView.WorldToClip));
float2 ObjectToScreen = float2( ((ObjectPos.xy / ObjectPos.w).x * 0.5 )+ 0.5 , (((ObjectPos.xy / ObjectPos.w).y * -0.5 ) + 0.5 ));

float2 Pos = (((ObjectToScreen - float2(0.5,0.5)) * float2(-1,-1))* (Offset) ) + float2(0.5,0.5);
Pos = float2(lerp(0.5,Pos.x,H),lerp(0.5,Pos.y,V));
float2 Coord = UV * ( 1/Size.xy ) - (Pos/Size.xy) + float2(0.5,0.5);
float Mask = ( step( Pos.x-(Size.x/2) , UV.x )* step( UV.x , Pos.x+(Size.x/2)) ) * ( step( Pos.y-(Size.y/2) , UV.y )* step( UV.y , Pos.y+(Size.y/2) ));

if( Mask > 0.0001000 )
{
Result += Texture2DSample( Tex,TexSampler, Coord.xy ).xyz * Mask.x;
return Result;
}
else
{
	return 0;
}


