//input TexObject : tex objecet , TexCoord : TexCoord, Dither : DitherTemporalAA, BlurIntensity : flaot 50


float shadow = 0;

float texelsize = 1./BlurIntensity*Dither;

for (int x = -1;x<= 1; ++x)

{

    for(int y = -1;y <= 1; ++y)

    {

        float TexR = Texture2DSample(TexObject,

TexObjectSampler,TexCoord + float2(x,y)*texelsize).r;

        shadow += TexR;

    }

}

shadow /= 9.;

return shadow;
