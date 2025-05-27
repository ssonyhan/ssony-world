//input SceneTexture : CustomDepth
// uv : ScreenPosition
// amount : scalar 0.5
// DrawDistance : scalar 100000.0


float3 res = float3(0.0f, 0.0f, 0.0f);

float2 invSize = View.ViewSizeAndInvSize.zw;

uv = ViewportUVToSceneTextureUV(uv, 14);

int TexIndex = 13;

const static float weights[25] = {
  0.01f, 0.02f, 0.04f, 0.02f, 0.01f,
  0.02f, 0.04f, 0.08f, 0.04f, 0.02f,
  0.04f, 0.08f, 0.16f, 0.08f, 0.04f,
  0.02f, 0.04f, 0.08f, 0.04f, 0.02f,
  0.01f, 0.02f, 0.04f, 0.02f, 0.01f
};

const static float offsets[5] = { -2.0f * amount, -1.0f * amount, 0.0f, 1.0f * amount, 2.0f * amount };

for (int i = 0; i < 5; ++i)
{
  float v_coord = uv.y + offsets[i] * invSize.y;
  int temp = i * 5;
  for (int j = 0; j < 5; ++j)
  {
    float u_coord = uv.x + offsets[j] * invSize.x;

    float2 uvShifted = float2(u_coord, v_coord);

    float weight = weights[temp + j];

    float3 texSample = SceneTextureLookup(uvShifted, TexIndex, false).rgb;

    float3 tex = clamp(texSample / DrawDistance, 0.0f, 1.0f);

    res += tex * weight;
  }
}

return float4(res, 1.0f);
