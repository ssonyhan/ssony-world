//input Range : scalar 1.0

static const int SceneTextureId = 14;
float2 InvSize = View.ViewSizeAndInvSize.zw;
float2 UV = GetSceneTextureUV(Parameters);

float SpiralTurns = 2.0;

float3 PixelColor = float3(0, 0, 0);
int NumIgnorePixels = 0;

int SampleCount = (2 * Range + 4) * (2 * Range + 4);

for (int i = 0; i < SampleCount; i++)
{
    
    float ratio = i / (float)(SampleCount - 1);
    float angle = ratio * SpiralTurns * 6.283185307f;
    float radius = ratio * Range;
    float2 offset = float2(cos(angle), sin(angle)) * radius * InvSize;
    float2 offsetUV = UV + offset;

    if (offsetUV.x < 0 || offsetUV.x > 1 || offsetUV.y < 0 || offsetUV.y > 1)
    {
        NumIgnorePixels++;
    }
    else
    {
        float3 currentColor = SceneTextureLookup(offsetUV, SceneTextureId, 0).rgb;
        PixelColor += currentColor;
    }
}

PixelColor /= (SampleCount - NumIgnorePixels);
return float4((PixelColor/2), 1);
