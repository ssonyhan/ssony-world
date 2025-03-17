float3 HalfVector = normalize(LightVector + WorldView);

// Use WorldNormal directly, NO Normal Map sampling
float3 displacedNormal = normalize(WorldNormal);

//Rotation around X-axis
float cosTheta = cos(rotationAngle);
float sinTheta = sin(rotationAngle);
float3 rotatedNormal = float3(displacedNormal.x, displacedNormal.y * cosTheta - displacedNormal.z * sinTheta, displacedNormal.y * sinTheta + displacedNormal.z * cosTheta);
displacedNormal = normalize(rotatedNormal);

float NdotH = saturate(dot(displacedNormal, HalfVector));

float EffectiveThreshold = HighlightThreshold + Roughness * (1 - HighlightThreshold);
float SpecularIntensity = smoothstep(EffectiveThreshold - 0.01, EffectiveThreshold + 0.01, NdotH);
float3 SpecularColor = HighlightColor * SpecularIntensity * HighlightIntensity;
return InColor + SpecularColor;