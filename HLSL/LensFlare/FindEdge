

//Input
//AbsoluteWorldPosition
//VertexNormal
//Edge_Range > Scalar
//Edge_Power > Scalar
//Edge_Range_Intensity > Scalar


float3 worldVertexNormal = VertexNormal; 
float3 worldPosition = AbsoluteWorldPosition; 


float3 ddxPosition = ddx(worldPosition);
float3 ddyPosition = ddy(worldPosition);
float3 crossNormal = normalize(cross(ddxPosition, ddyPosition));
float distanceValue = length(worldVertexNormal - crossNormal);


float edgeIntensity = pow(distanceValue, Edge_Range) * Edge_Range_Intensity;
float edgeEffect = saturate(pow(edgeIntensity, Edge_Power));


return edgeEffect;
