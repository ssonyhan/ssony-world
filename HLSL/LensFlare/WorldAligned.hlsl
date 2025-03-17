
float3 WorldPosition = AbsoluteWorldPosition; 
float3 VertexNormal = abs(VertexNormalWS); 

float3 UV = WorldPosition / TextureSize;
UV = abs(UV); 
UV = UV * -1.0f; 

float U = UV.r;
float V = UV.g;
float W = UV.b;

float4 Color1 = Texture.SampleLevel(TextureSampler, float2(V, W), 1.0); //X
float4 Color2 = Texture.SampleLevel(TextureSampler, float2(U, W), 1.0); //Y
float4 Color3 = Texture.SampleLevel(TextureSampler, float2(U, V), 1.0); //Z

float4 InterpolatedColor = lerp(Color2, Color1, VertexNormal.r); 
return lerp(InterpolatedColor, Color3, VertexNormal.b);




////// Z aligned 

float3 WorldPosition = AbsoluteWorldPosition; 

float3 UV = WorldPosition / TextureSize;
UV = abs(UV); 
UV = UV * -1.0f; 

float U = UV.r;
float V = UV.g;
float W = UV.b;


float4 Color3 = Texture.SampleLevel(TextureSampler, float2(U, V), 1.0); //Z
return Color3;




///bump offset 

// Input Pin (T)
float3 WorldPosition = AbsoluteWorldPosition; 
float3 VertexNormal = abs(VertexNormalWS); 

// Camera Vector (normalized)
float3 CameraVector = normalize(CameraVectorWS);

// Adjusted UV for Bump Offset
float3 UV = WorldPosition / TextureSize;
UV = abs(UV);

// Bump Offset Parameters
float HeightScale = 0.05f;   // 파라미터로 변환
float Bias = HeightScale * 0.5f; // Shifts depth map range

// Depth Texture Sample (grayscale assumed)
float Height = Texture.SampleLevel(TextureSampler, float2(UV.r, UV.g), 0.0).r;

// Apply Bump Offset
float2 Offset = Height * HeightScale * CameraVector.xy / CameraVector.z;
UV.xy += Offset - Bias;

// Clamped UVs to prevent artifacts
UV = saturate(UV);

// Recompute individual UV channels
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
