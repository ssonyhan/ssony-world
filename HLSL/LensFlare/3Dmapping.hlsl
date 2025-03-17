

// Input Pin (T)
float3 WorldPosition = AbsoluteWorldPosition; 
float3 VertexNormal = abs(VertexNormalWS); 

float3 UV = WorldPosition / TextureSize;
UV = abs(UV); 
UV = UV * -1.0f; 

float U = UV.r;
float V = UV.g;
float W = UV.b;

// Texture Sampling & Masked UV
float4 Color1 = Texture.SampleLevel(TextureSampler, float2(V, W), 1.0); //X
float4 Color2 = Texture.SampleLevel(TextureSampler, float2(U, W), 1.0); //Y
float4 Color3 = Texture.SampleLevel(TextureSampler, float2(U, V), 1.0); //Z

// Final Output
float4 InterpolatedColor = lerp(Color2, Color1, VertexNormal.r); 
return lerp(InterpolatedColor, Color3, VertexNormal.b);
