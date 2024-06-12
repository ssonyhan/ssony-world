import unreal 
from Lib import __lib_topaz__ as topaz


desired_triangle_percentage : float = 0.33

assets = topaz.get_selected_assets()
## execution here ##
for each in assets :
                
    if each.__class__ == unreal.StaticMesh : 
        if each is not None : 

            nanite_settings : unreal.MeshNaniteSettings     = each.get_editor_property('nanite_settings')
            nanite_settings.enabled = True

            getTrianglePercent = nanite_settings.get_editor_property('keep_percent_triangles')

            if getTrianglePercent >= desired_triangle_percentage :
                nanite_settings.keep_percent_triangles = desired_triangle_percentage 
                print(getTrianglePercent) 
                each.set_editor_property('nanite_settings', nanite_settings)

            else : # getTrianglePercent < desired_triangle_percentage 
                pass
                print('pass')
 
print('OK')


