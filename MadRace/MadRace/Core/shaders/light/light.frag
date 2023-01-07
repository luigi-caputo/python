varying vec4 color;
varying vec3 normal;
varying vec4 vertex;

void main()
{
vec3 vectorPos = (gl_ModelViewMatrix*vertex).xyz;
vec3 lightPos = normalize(gl_LightSource[0].position.xyz - vectorPos);
vec3 normalPos = (gl_NormalMatrix*normal).xyz;

float lightIntensity = max(0.0, dot(normalPos, lightPos));

gl_FragColor.rgb = color.rgb * lightIntensity;
gl_FragColor.rgb += gl_LightModel.ambient.rgb;

vec3 reflectionPos = normalize(reflect(-lightPos, normalPos));

float specular = max(0.0, dot(normalPos, reflectionPos));

if(lightIntensity != 0.0){
float specularf = pow(specular, 160f); //gl_FrontMaterial.shininess
gl_FragColor += specularf;
}
} 
