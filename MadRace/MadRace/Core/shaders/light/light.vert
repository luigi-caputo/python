varying vec4 color;
varying vec3 normal;
varying vec4 vertex;
void main()
{
  normal = gl_Normal;
  vertex = gl_Vertex;
  color = gl_Color;
  gl_Position = gl_ModelViewProjectionMatrix*gl_Vertex;
}
