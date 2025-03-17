// RadialDistorsionUV
// By Cyberalien 2023

// UV -> TexCoord
// UVGrad -> TexCoord
// POS
// Radius -> Float
// Density -> Float
// Intensity -> Float

// Radial Gradient Expo
float2 RGEx_UV;
float2 RGEx_POS; 
float RGEx_Radius; 
float RGEx_Density;
float RGEx_Intensity;

RGEx_UV = UVGrad - 0.5 ;
RGEx_POS = float2( 0 , 0 );
RGEx_Radius = Radius ;
RGEx_Density = Density ;
RGEx_Intensity = Intensity;

float RGEx_BaseMask = 1 - (distance( RGEx_UV , RGEx_POS )/RGEx_Radius);
float RGEx_Expo = 1/PositiveClampedPow(2.71828198,(RGEx_BaseMask*RGEx_Density)*(RGEx_BaseMask*RGEx_Density));
float RGEx_RadialExpoMask = 0 ;
if ( RGEx_BaseMask > 0 )
{
	RGEx_RadialExpoMask = 1 - RGEx_Expo ;
}
return UV - ( RGEx_UV * RGEx_RadialExpoMask * RGEx_Intensity )  ;