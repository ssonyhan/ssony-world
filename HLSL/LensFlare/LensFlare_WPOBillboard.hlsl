// WPO billboard
// By CyberAlien

// DistanceToCamera
float3 ObjectPos = LWCToFloat(GetObjectWorldPosition(Parameters));
float3 CamPos = LWCToFloat(ResolvedView.WorldCameraOrigin);

return (DistanceToCamera - distance(ObjectPos , CamPos) )*(normalize(ObjectPos - CamPos));

