float3 WorldPosition = WP; // Get world position

// Capsule Axis
float3 CapsuleAxis = normalize(CapsuleEnd - CapsuleStart);

// Project WorldPosition onto Capsule Axis
float t = dot(WorldPosition - CapsuleStart, CapsuleAxis);
float capsuleLength = length(CapsuleEnd - CapsuleStart);
t = saturate(t / capsuleLength); // Clamp t to 0-1 range

// Closest point on the capsule axis
float3 ClosestPoint = CapsuleStart + t * (CapsuleEnd - CapsuleStart);

// Vector from closest point to WorldPosition
float3 Dir = WorldPosition - ClosestPoint;
float distToAxis = length(Dir);

float2 uv = float2(0, 0);
float3 normal = float3(0, 0, 0);
float3 tangent = float3(0, 0, 0);
float3 bitangent = float3(0, 0, 0);

// Check which part of the capsule the point is on
if (distToAxis <= CapsuleRadius && t > 0 && t < 1)
{
    // Cylinder UV generation
    float3 right = normalize(cross(CapsuleAxis, float3(0, 1, 0)));
    float angle = atan2(dot(Dir, right), dot(Dir, cross(right, CapsuleAxis)));
    uv = float2(angle / (2 * PI), t);
    normal = normalize(Dir);
    tangent = CapsuleAxis;
    bitangent = normalize(cross(normal, tangent));
}
else if (t <= 0)
{
    // Top Hemisphere
    uv = GenerateSphereUV_Top;
    normal = normalize(Dir);
    tangent = normalize(cross(normal, CapsuleAxis)); // Improved tangent calculation
    bitangent = normalize(cross(normal, tangent));
}
else
{
    // Bottom Hemisphere
    uv = GenerateSphereUV_Bottom;
    normal = -normalize(Dir);                        // Normal points inward for bottom hemisphere
    tangent = normalize(cross(normal, CapsuleAxis)); // Improved tangent calculation
    bitangent = normalize(cross(normal, tangent));
}

// Normalize vectors
LightVector = normalize(LightVector);
ViewDirection = normalize(ViewDirection);

// Calculate halfway vector
float3 HalfwayVector = normalize(LightVector + ViewDirection);

// Calculate curvature factor
float curvatureFactor = 1.0 - abs(dot(normal, CapsuleAxis));
curvatureFactor = saturate(curvatureFactor); // Clamp to 0-1 range

// Calculate view angle
float viewAngle = acos(dot(normalize(CapsuleAxis), normalize(ViewDirection)));

// View-dependent rim threshold
float rimThreshold = 0.7 + 0.3 * viewAngle / PI; // Adjust coefficients as needed
rimThreshold = saturate(rimThreshold);           // Clamp to 0-1 range

// Rim Lighting Calculation:
float NdotV = saturate(1.0 - dot(normal, ViewDirection));
float RimIntensity = smoothstep(rimThreshold, 1.0, NdotV);
RimIntensity = pow(RimIntensity, RimPower);

// Specular calculation with curvature factor
float NdotH = saturate(dot(normal, HalfwayVector));
float SpecularIntensity = pow(NdotH, 100.0 * (1.0 - Roughness)) * curvatureFactor;

// Combine specular and rim lighting (adjust weighting as needed)
return SpecularColor * SpecularIntensity + RimColor * RimIntensity;