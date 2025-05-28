
//input SceneTexture
//uv = custom /* return GetSceneTextureUV(Parameters); */ => CMOT flaot2
//res = viewsize


float2 sobelMatrix[9] = { float2(-1, -1), float2(0, -2), float2(1, -1),
                          float2(-1,  0), float2(0,  0), float2(1,  0),
                          float2(-1,  1), float2(0,  2), float2(1,  1) };

float intensity = 1.0;
float2 gradients = 0.0;

for (int i = 0; i < 9; ++i)
{
    int row = i / 3; // Current Row
    int col = i % 3; // Current Column

    // Get Neighbouring Pixel Offset
    float offsetX = (col - 1) / res.x;
    float offsetY = (row - 1) / res.y;

    float2 offsetUV = float2(uv.x + offsetX,
                             uv.y + offsetY);

    float sampledIntensity = SceneTextureLookUp(offsetUV, 14, false);   
    // scenecolor = 0, customdepth=13, ppinput0=14, customstencil=24

    gradients += sobelMatrix[i] * sampledIntensity;
}

gradients *= intensity;
return length(gradients);
