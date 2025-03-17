// LensFlare Billboard Ghost noise

// Tex -> Tex2D
// Step -> flaot
// UV -> Distortion UV 
// GlobalSize -> flaot 1.96
// GlobalPos -> flaot 0.68
// TexNoise -> Tex2D
// NoiseOffset -> flaot
// BaseValue -> flaot
// TexTint -> Tex2D
// TintIntensity -> flaot
// OffsetStart -> flaot
// H -> flaot
// V -> flaot
float2 Coord;
float2 ScaleCoord;
float2 Pos;
float NewSize;
float2 NewCoord;
float Mask;
float Size;
float2 ScaleAngle;
float3 Result = 0;
float2 SizeNoiseUV;
float2 PosNoiseUV;
float2 TintUV;
float SizeKernel;
float PosKernel;
float BaseSizeKernel[8] = 
{
	{ 0.12 },{ 0.09 },{ 0.05 },{ 0.01 },{ 0.1 },{ 0.02 },{ 0.18 },{ 0.14 }
};
float BasePosKernel[8] = 
{
	{ 0.05 },{ 0.15 },{ 0.35 },{ 0.41 },{ 0.67 },{ 0.79 },{ 0.82 },{ 0.95 }
};

float4 ObjectPos = mul(float4(LWCToFloat(GetObjectWorldPosition(Parameters)).xyz,1),LWCToFloat(ResolvedView.WorldToClip));
float2 ObjectToScreen = float2( ((ObjectPos.xy / ObjectPos.w).x * 0.5 )+ 0.5 , (((ObjectPos.xy / ObjectPos.w).y * -0.5 ) + 0.5 ));

for ( int i = 0 ; i<Step ; i++)
{
	SizeNoiseUV = float2( (i/Step)%1, (NoiseOffset-(1/5))% 1 );
	PosNoiseUV = float2( (i/Step)%1, (NoiseOffset-(1/2))% 1 );
	SizeKernel = lerp(Texture2DSample( TexNoise ,TexSampler, frac(SizeNoiseUV) ).x * BaseSizeKernel[i%7] , BaseSizeKernel[i%7] , BaseValue ) ;
	PosKernel = lerp(Texture2DSample( TexNoise ,TexSampler, frac(PosNoiseUV) ).x * BasePosKernel[i%7] , BasePosKernel[i%7] , BaseValue ) ;
//	TintUV = frac(float2( SizeKernel , PosKernel ));
	TintUV = frac( SizeNoiseUV + PosNoiseUV + (i/Step) );
	//
	Size = SizeKernel*GlobalSize ;
	Pos = (((ObjectToScreen - float2(0.5,0.5)) * float2(-1,-1))* ((PosKernel*GlobalPos)+OffsetStart) ) + float2(0.5,0.5);
	Pos = float2(lerp(0.5,Pos.x,H),lerp(0.5,Pos.y,V));
	float2 Coord = UV * ( 1/Size ) - (Pos/Size) + float2(0.5,0.5);
	float Mask = ( step( Pos.x-(Size/2) , UV.x )* step( UV.x , Pos.x+(Size/2)) ) * ( step( Pos.y-(Size/2) , UV.y )* step( UV.y , Pos.y+(Size/2) ));
	if ( Mask > 0.0001000 )
	{
	Result += Texture2DSample( Tex,TexSampler, saturate(Coord.xy) ).xyz * Mask.x * ( 1- SizeKernel ) * lerp( 1 , Texture2DSample( TexTint , TexSampler , TintUV ).xyz , TintIntensity );
	}
}
return Result;