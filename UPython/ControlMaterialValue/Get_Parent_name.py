import unreal
from Lib import __lib_topaz__ as topaz
import importlib

importlib.reload(topaz)

selected_assets = topaz.get_selected_assets() 

for each in selected_assets :
    print(each.get_name())
    if each.__class__ == unreal.MaterialInstanceConstant :

        get_master_mat = each.get_editor_property('parent')
        print(get_master_mat)

        if get_master_mat.__class__ == unreal.MaterialInstanceConstant :
            print("Have Depth")

        else :
            pass

    else :
        print("Not MaterialInstance")
