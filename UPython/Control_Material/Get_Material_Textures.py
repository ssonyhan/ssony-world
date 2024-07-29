
'''

import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()



def testGraphTraversalBackwardTrace(mat, prop = unreal.MaterialProperty.MP_EMISSIVE_COLOR):
    output_node = unreal.MaterialEditingLibrary.get_material_property_input_node(mat, prop)
    assert output_node != None, "No Output in selected property "+ str(prop) +" in material "+mat.get_name()

    inputs = unreal.MaterialEditingLibrary.get_inputs_for_material_expression(mat, output_node)
    if len(inputs) == 0:
        print("Found input node")
    else:
        for i, node in enumerate(inputs):
            if node == None:
                print("input not connected")
            else:
                print("Node " +node.get_name() +" connected to pin"+str(i) + " of node " + output_node.get_name())
                # WHICH output pin of node is connected?               
            

for i in selected_assets : 
    testGraphTraversalBackwardTrace(i)

'''


import unreal

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

def basecolortexturereplace(source_mat, base_property = unreal.MaterialProperty.MP_BASE_COLOR) :
    output_node = unreal.MaterialEditingLibrary.get_material_property_input_node(source_mat, base_property)

    inputs = unreal.MaterialEditingLibrary.get_inputs_for_material_expression(source_mat, output_node)
    get_tex = unreal.MaterialEditingLibrary.get_used_textures(source_mat)

    if len(inputs) == 0:
        print("Found BaseColorinput node")

    else :
        for i, node in enumerate(inputs) :
            if node == None :
                print("인풋 없음")
            
            else :
                print(get_tex)


for select_mat in selected_assets :
    basecolortexturereplace(select_mat)


    




        


